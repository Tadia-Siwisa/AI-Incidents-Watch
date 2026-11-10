#!/usr/bin/env python3
"""Stage source-linked AI-agent research updates. Never writes to reviewed datasets.

Triggered by an owner-authored [Evidence] GitHub issue or workflow_dispatch.
The canonical state is data/intake/incoming_evidence.json; XLSX is a generated view.
"""
from __future__ import annotations

import json
import os
import re
from urllib.request import Request, urlopen
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "intake"
JSON_FILE = OUT / "incoming_evidence.json"
WORKBOOK_FILE = OUT / "incoming_evidence.xlsx"
ALLOWED_CHANGE_TYPES = {
    "New candidate", "Update to existing case",
    "Correction or retraction", "Relevant research / context",
    "Unknown — needs review",
}
COLUMNS = [
    ("intake_id", "Intake ID", 16),
    ("report_title", "Report / disclosure", 42),
    ("source_url", "Primary source URL", 55),
    ("disclosure_date", "Disclosure date", 18),
    ("incident_date", "Incident date", 22),
    ("change_type", "New / update / correction", 26),
    ("related_case", "Existing case / suspected match", 38),
    ("context", "Evidence context", 35),
    ("reported_actions", "Reported action / findings", 64),
    ("new_evidence", "What's new / changed", 64),
    ("uncertainties", "Evidence limitations / caveats", 64),
    ("found_by", "Discovery channel", 24),
    ("review_status", "Review status", 20),
    ("possible_duplicate_of", "Possible duplicate of", 20),
    ("issue_url", "GitHub intake issue", 48),
    ("updated_at", "Last staged", 24),
]


def issue_fields(body: str) -> dict[str, str]:
    parts = re.split(r"(?m)^### (.+?)\s*$", body or "")
    return {parts[i].strip().casefold(): parts[i + 1].strip()
            for i in range(1, len(parts) - 1, 2)}


def safe_text(value: object, limit: int = 12000) -> str:
    text = str(value or "").strip()
    if len(text) > limit:
        raise ValueError("Evidence field is too long")
    return text if text not in ("_No response_", "None") else ""


def canonical_url(raw: str) -> str:
    url = urlsplit(raw.strip().strip("<>"))
    if url.scheme.lower() not in ("http", "https") or not url.netloc:
        raise ValueError("A valid public http(s) primary source URL is required")
    if url.username or url.password:
        raise ValueError("Credentials must not appear in source URLs")
    host = (url.hostname or "").lower()
    if host in ("localhost", "127.0.0.1", "::1"):
        raise ValueError("A public source URL is required")
    netloc = host + ((":" + str(url.port)) if url.port else "")
    path = (url.path or "/").rstrip("/") or "/"
    query = urlencode(
        [(k, v) for k, v in parse_qsl(url.query, keep_blank_values=True)
         if not k.lower().startswith(("utm_", "mc_")) and
         k.lower() not in ("fbclid", "gclid", "trk")], doseq=True
    )
    return urlunsplit((url.scheme.lower(), netloc, path, query, ""))


def make_record(issue: dict, owner: str) -> dict:
    if issue.get("user", {}).get("login") != owner:
        raise ValueError("Only owner-authored [Evidence] issues can enter the register")
    if not str(issue.get("title", "")).startswith("[Evidence]"):
        raise ValueError("Not an evidence-intake issue")
    f = issue_fields(issue.get("body", ""))
    required = ("report title", "primary source url", "reported actions / findings")
    if any(not safe_text(f.get(k)) for k in required):
        raise ValueError("Missing required evidence-intake fields")
    url = safe_text(f["primary source url"]).split()[0].strip("<>")
    normalized = canonical_url(url)
    change = safe_text(f.get("update type")) or "Unknown — needs review"
    if change not in ALLOWED_CHANGE_TYPES:
        change = "Unknown — needs review"
    number = int(issue["number"])
    return {
        "intake_id": f"EV-{number:05d}",
        "issue_number": number,
        "issue_url": safe_text(issue.get("html_url")),
        "report_title": safe_text(f["report title"], 400),
        "source_url": url,
        "canonical_source_url": normalized,
        "disclosure_date": safe_text(f.get("disclosure date"), 80),
        "incident_date": safe_text(f.get("incident date"), 120),
        "change_type": change,
        "related_case": safe_text(f.get("related case"), 200),
        "context": safe_text(f.get("evidence context"), 300),
        "reported_actions": safe_text(f["reported actions / findings"]),
        "new_evidence": safe_text(f.get("new evidence or correction")),
        "uncertainties": safe_text(f.get("uncertainties and verification gaps")),
        "found_by": safe_text(f.get("discovery channel"), 100) or "Unknown",
        "review_status": "Pending review",
        "possible_duplicate_of": "",
        "first_seen_at": safe_text(issue.get("created_at"), 80),
        "updated_at": safe_text(issue.get("updated_at"), 80),
    }


def rebuild_duplicate_flags(rows: list[dict]) -> None:
    """Flag possible duplicate evidence URLs; never deduplicate distinct claims blindly."""
    seen: dict[tuple, str] = {}
    for row in sorted(rows, key=lambda x: x["issue_number"]):
        row["possible_duplicate_of"] = ""
        key = (row.get("canonical_source_url", ""),
               row.get("disclosure_date", "").strip(),
               row.get("related_case", "").casefold().strip())
        if key in seen:
            row["possible_duplicate_of"] = seen[key]
        else:
            seen[key] = row["intake_id"]


def read_rows() -> list[dict]:
    if not JSON_FILE.exists():
        return []
    value = json.loads(JSON_FILE.read_text(encoding="utf-8"))
    if not isinstance(value, list):
        raise ValueError("incoming_evidence.json must contain a list")
    return value


def excel_safe(value: object):
    if isinstance(value, str) and value.startswith(("=", "+", "-", "@")):
        return "'" + value
    return value


def write_workbook(rows: list[dict]) -> None:
    wb = Workbook()
    guide = wb.active
    guide.title = "READ FIRST"
    guide.append(["INCOMING EVIDENCE — UNVERIFIED SOURCE INTAKE"])
    guide.append(["This file is generated automatically from GitHub [Evidence] issues."])
    guide.append(["Rows may be unverified, duplicated, or later corrected."])
    guide.append(["It is not a list of confirmed agent incidents or an approved dataset."])
    guide.append(["Review and discuss entries before any changes to data/working/."])
    guide.append(["Duplicates are flagged by source URL + disclosure date + case match."])
    guide.append(["Source: data/intake/incoming_evidence.json"])
    guide.column_dimensions["A"].width = 105
    guide["A1"].font = Font(size=14, bold=True, color="17365D")
    for i in range(2, 8):
        guide[f"A{i}"].alignment = Alignment(wrap_text=True)
    sheet = wb.create_sheet("Pending evidence")
    sheet.append([label for _, label, _ in COLUMNS])
    sheet.freeze_panes = "D2"
    sheet.auto_filter.ref = f"A1:P{max(2, len(rows) + 1)}"
    for col, (_, _, width) in enumerate(COLUMNS, 1):
        sheet.column_dimensions[get_column_letter(col)].width = width
        cell = sheet.cell(1, col)
        cell.fill = PatternFill("solid", fgColor="17365D")
        cell.font = Font(color="FFFFFF", bold=True)
        cell.alignment = Alignment(wrap_text=True, vertical="center")
    sheet.row_dimensions[1].height = 32
    for row in rows:
        sheet.append([excel_safe(row.get(key, "")) for key, _, _ in COLUMNS])
        n = sheet.max_row
        sheet.row_dimensions[n].height = 64
        for c in sheet[n]:
            c.alignment = Alignment(wrap_text=True, vertical="top")
        for column in (3, 15):
            c = sheet.cell(n, column)
            if str(c.value).startswith(("http://", "https://")):
                c.hyperlink = c.value
                c.style = "Hyperlink"
        if row["possible_duplicate_of"]:
            sheet.cell(n, 14).fill = PatternFill("solid", fgColor="FFF2CC")
    tmp = WORKBOOK_FILE.with_name(WORKBOOK_FILE.name + ".tmp")
    wb.save(tmp)
    tmp.replace(WORKBOOK_FILE)


def fetch_repository_evidence_issues() -> list[dict]:
    """Reconcile all owner-authored evidence issues, not only the triggering event.

    This also recovers items lost if an earlier GitHub Actions run was cancelled
    or overlapped with another update. All rows remain pending review.
    """
    token = os.environ.get("GITHUB_TOKEN", "")
    repository = os.environ.get("GITHUB_REPOSITORY", "")
    if not token or "/" not in repository:
        raise ValueError("GITHUB_TOKEN and GITHUB_REPOSITORY required for issue reconciliation")
    owner = repository.split("/", 1)[0]
    found = []
    page = 1
    while True:
        url = (
            f"https://api.github.com/repos/{repository}/issues"
            f"?state=all&per_page=100&page={page}"
        )
        req = Request(url, headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "AI-Incidents-Watch-evidence-reconcile",
            "X-GitHub-Api-Version": "2022-11-28",
        })
        with urlopen(req, timeout=25) as response:
            batch = json.load(response)
        if not isinstance(batch, list):
            raise ValueError("Unexpected GitHub issue list response")
        for issue in batch:
            if "pull_request" in issue:
                continue
            if (issue.get("user", {}).get("login") == owner
                    and str(issue.get("title", "")).startswith("[Evidence]")):
                found.append(issue)
        if len(batch) < 100:
            break
        page += 1
        if page > 50:
            raise ValueError("Unexpectedly large issue pagination")
    return found


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = read_rows()
    # Always rebuild the queue from all authorized evidence issues, so a burst
    # of issue creations cannot leave some issues absent from the Excel register.
    # Existing manual review status is preserved across the reconciliation.
    for issue in fetch_repository_evidence_issues():
        row = make_record(issue, os.environ["GITHUB_REPOSITORY"].split("/", 1)[0])
        prior = next((r for r in rows if r["issue_number"] == row["issue_number"]), None)
        if prior:
            row["first_seen_at"] = prior.get("first_seen_at") or row["first_seen_at"]
            row["review_status"] = prior.get("review_status", "Pending review")
        rows = [r for r in rows if r["issue_number"] != row["issue_number"]]
        rows.append(row)
    rows.sort(key=lambda r: r["issue_number"])
    rebuild_duplicate_flags(rows)
    JSON_FILE.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_workbook(rows)
    print(f"Incoming evidence: {len(rows)} entries, "
          f"{sum(bool(r['possible_duplicate_of']) for r in rows)} possible duplicates. "
          "No reviewed dataset was changed.")


if __name__ == "__main__":
    main()
