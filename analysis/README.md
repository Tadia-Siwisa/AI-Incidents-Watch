# Exploratory analysis layer

This directory contains conservative analytical coding derived from the
adjudicated case findings in `data/rebuilt/factual_rebuild.json`.

- `case_coding.csv` and `case_coding.json` contain one row per canonical case
  family. Multi-label values use `|` as a separator.
- `summary.json` contains headline counts checked by the analysis script.
- `tables/` contains the aggregate tables used in the research report.

Run the analysis from the repository root:

```bash
python scripts/analyze_incidents.py
```

The script validates that all 46 factual case families are coded exactly once,
then regenerates the data files, tables, and report figures. The analytical
codes do not replace the factual rebuild. An allegation is coded as alleged,
controlled behavior remains controlled, and missing details remain unknown.
Category counts are case-family counts. Multi-label action and effect totals
can exceed the number of cases.

