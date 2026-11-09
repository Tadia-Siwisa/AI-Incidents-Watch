# Research artifacts — reports, scripts, and sources

This page provides a stable entry point to the repository's **existing research outputs**. They remain in their established directories so scripts and references continue to work. The research log and agenda are standalone in this `research/` directory.

## Canonical documentation
- [Chronological research log](RESEARCH_LOG.md)
- [Working research agenda and questions](RESEARCH_AGENDA.md)
- [Repository introduction and historical stages](../README.md)
- [Source evidence verification notes](../VERIFICATION.md)
- [Incident intake documentation](../docs/INCIDENT_INTAKE.md)

## Reports already in the repository
- [Exploratory analysis report (Markdown)](../reports/AI_Agent_Incident_Exploratory_Analysis.md)
- [Exploratory analysis report (PDF)](../reports/AI_Agent_Incident_Exploratory_Analysis.pdf)
- [Report figures](../reports/figures/)

## Analysis and evidence tables already in the repository
- [Analysis guide](../analysis/README.md)
- [Analysis tables](../analysis/tables/)
- [Historical 46-case factual rebuild](../data/rebuilt/factual_rebuild.json)
- [30 October 188-source evidence snapshot](../data/working/review_snapshot_2026-10-30/188_evidence_ledger.csv)

## Existing scripts (not moved)
- [Incident analysis](../scripts/analyze_incidents.py)
- [Factual rebuild](../scripts/build_factual_rebuild.py)
- [Evidence-update builder](../scripts/build_evidence_updates.py)
- [Master reading-list builder](../scripts/build_master_reading_list.py)
- [Research PDF builder](../scripts/build_research_pdf.py)
- [Wide Search 2 builder](../scripts/build_wide_search_2.py)
- [Incident intake updater](../scripts/update_incident_intake.py)
- [All existing scripts](../scripts/)

## Important files not yet present in this GitHub repository

The following were generated separately in the ChatGPT file library/workspace and **have not been added to this GitHub repository** by this documentation change:

- `AI_Incident_Watch_188_Full_Category_Fit_Pass_2026-11-09.xlsx` — working five-category source classification.
- `AI_Incident_Watch_188_Source_Reading_File_2026-11-09.xlsx` — plain-language source reading list.
- `AI_Incident_Watch_Full_188_Reconciliation_2026-11-07.xlsx` — source-to-episode reconciliation.
- `AI_Incident_Watch_188_Research_Log_and_Agenda_2026-11-09.xlsx` — original combined workbook; key methodological content is now preserved in standalone Markdown files here.

**Handling rule:** Dataset exports belong under `data/` (or a dedicated dated data-snapshot location); interpretation, decisions and session notes belong under `research/`; executable scripts stay in `scripts/`; analysis outputs stay in `analysis/` and reports in `reports/`. This index brings them together **without duplicating or relocating files**.
