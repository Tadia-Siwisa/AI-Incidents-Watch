#!/usr/bin/env python3
"""Render the complete Markdown research report as a polished A4 PDF."""

from __future__ import annotations

import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "reports/AI_Agent_Incident_Exploratory_Analysis.md"
OUTPUT = ROOT / "reports/AI_Agent_Incident_Exploratory_Analysis.pdf"
GITHUB_BLOB = "https://github.com/Tadia-Siwisa/AI-Incidents-Watch/blob/main/"

LATEX_HEADER = r"""
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage{microtype}
\usepackage{fancyhdr}
\definecolor{reportnavy}{HTML}{17365D}
\definecolor{reportblue}{HTML}{2F75B5}
\AtBeginDocument{\hypersetup{colorlinks=true,linkcolor=reportnavy,urlcolor=reportblue,citecolor=reportblue}}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\color{reportnavy}AI Incident Watch}
\fancyhead[R]{\small\color{reportnavy}Exploratory research report}
\fancyfoot[C]{\thepage}
\setlength{\headheight}{14pt}
\setlength{\tabcolsep}{4pt}
\renewcommand{\arraystretch}{1.18}
\setlength{\LTpre}{5pt}
\setlength{\LTpost}{8pt}
\setlength{\emergencystretch}{3em}
"""

TABLE_FILTER = r"""
local stringify = pandoc.utils.stringify

function Table(t)
  if not t.head or not t.head.rows or #t.head.rows == 0 then return t end
  local cells = t.head.rows[1].cells
  if #cells == 0 then return t end
  local first = stringify(cells[1].contents)
  local widths
  if first == 'Source register' then
    widths = {0.27, 0.13, 0.60}
  elseif first == 'Population' then
    widths = {0.22, 0.43, 0.08, 0.27}
  elseif first == 'Factual disposition' then
    widths = {0.24, 0.10, 0.12, 0.54}
  elseif first == 'Case' then
    widths = {0.07, 0.17, 0.18, 0.18, 0.19, 0.21}
  elseif #cells == 3 then
    widths = {0.55, 0.22, 0.23}
  end
  if widths then
    for i, spec in ipairs(t.colspecs) do
      t.colspecs[i] = {spec[1], widths[i]}
    end
  end
  return t
end
"""


def command_path(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise RuntimeError(f"Required command not found: {name}")
    return path


def build() -> None:
    pandoc = command_path("pandoc")
    command_path("xelatex")

    markdown = SOURCE.read_text(encoding="utf-8")
    markdown = re.sub(
        r"^# Exploratory analysis of reported AI-agent incidents\s*\n", "", markdown, count=1
    )
    markdown = re.sub(
        r"\]\(\.\./([^)]+)\)",
        lambda match: f"]({GITHUB_BLOB}{match.group(1)})",
        markdown,
    )
    # The slash prevents TeX from finding a line-break opportunity in a narrow table cell.
    markdown = markdown.replace("Investigation/disclosure documented", "Investigation and disclosure documented")
    title_block = """---
title: "Exploratory analysis of reported AI-agent incidents"
subtitle: "Evidence-aware review of 46 reconciled case families"
date: "Evidence cut-off 9 October 2026 · Analysis date 13 October 2026"
---

"""

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="ai-incident-report-") as temp_dir:
        temp = Path(temp_dir)
        markdown_path = temp / "report.md"
        header_path = temp / "report-header.tex"
        filter_path = temp / "table-widths.lua"
        home_path = temp / "home"
        cache_path = temp / "cache"
        texmf_path = temp / "texmf-var"
        for path in (home_path, cache_path, texmf_path):
            path.mkdir(parents=True, exist_ok=True)
        markdown_path.write_text(title_block + markdown, encoding="utf-8")
        header_path.write_text(LATEX_HEADER, encoding="utf-8")
        filter_path.write_text(TABLE_FILTER, encoding="utf-8")

        environment = {
            **os.environ,
            "HOME": str(home_path),
            "XDG_CACHE_HOME": str(cache_path),
            "TEXMFVAR": str(texmf_path),
            "SOURCE_DATE_EPOCH": "1791892800",
        }
        result = subprocess.run(
            [
                pandoc,
                str(markdown_path),
                "--from=gfm",
                "--pdf-engine=xelatex",
                "--toc",
                "--toc-depth=2",
                f"--resource-path={SOURCE.parent}",
                f"--lua-filter={filter_path}",
                "--variable=papersize:a4",
                "--variable=geometry:margin=18mm",
                "--variable=fontsize:10pt",
                "--variable=classoption:titlepage",
                "--variable=mainfont:DejaVu Serif",
                "--variable=sansfont:DejaVu Sans",
                "--variable=monofont:DejaVu Sans Mono",
                f"--include-in-header={header_path}",
                f"--output={OUTPUT}",
            ],
            cwd=SOURCE.parent,
            env=environment,
            capture_output=True,
            text=True,
            timeout=120,
        )
        if result.returncode:
            raise RuntimeError(
                f"Pandoc PDF render failed ({result.returncode}):\n"
                f"{result.stdout[-2000:]}\n{result.stderr[-4000:]}"
            )

    if not OUTPUT.exists() or OUTPUT.stat().st_size < 100_000:
        raise RuntimeError("PDF was not created or is unexpectedly small")
    print(f"Built {OUTPUT.relative_to(ROOT)} ({OUTPUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    build()
