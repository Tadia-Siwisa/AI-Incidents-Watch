# Research datasets and source records

The `data/` folder is for **data**, not published research or documentation.

| Folder | Meaning |
| --- | --- |
| [working/](working/) | Current evidence-ledger snapshots under active analysis |
| [history/2026-10/](history/2026-10/) | Earlier Excel workbook versions, preserving their original filenames and bytes |
| [original/](original/) | Original narrow, wide and Reddit input workbooks |
| [rebuilt/](rebuilt/) | Reconciled 46-family factual/claim records and provenance |
| [wide_search_2/](wide_search_2/) | Expanded discovery material and machine-readable register |
| [monitoring/](monitoring/) | Dated source scans, source-change tracking and raw discovery |
| [intake/](intake/) | Incoming **unverified** incident leads from GitHub Issues |

**Current GitHub-hosted 188-source snapshot:** [188_evidence_ledger.csv, 30 October 2026](working/review_snapshot_2026-10-30/188_evidence_ledger.csv).

**Current reviewed workbooks (9 November 2026):** [188-source category-fit classification audit](working/2026-11-09/AI_Incident_Watch_188_Full_Category_Fit_Pass_2026-11-09.xlsx) and [plain-language 188-source reading file](working/2026-11-09/AI_Incident_Watch_188_Source_Reading_File_2026-11-09.xlsx). These are the original reviewed Excel workbooks, preserved in full, not CSV re-creations. The October 30 ledger remains the dated input snapshot.

The four files under [history/2026-10/](history/2026-10/) have different historical purposes: original reading list, 225-candidate wide search workbook, earlier combined 46/wide view, and dated evidence updates. The files were moved intact rather than deleted; Git retains previous locations.

## Separate automatic evidence intake (not yet reviewed)

New disclosures and corrections are staged into [incoming_evidence.xlsx](intake/incoming_evidence.xlsx) and its [source JSON](intake/incoming_evidence.json). **These are unverified reports, not confirmed incidents and not the working 188-source workbook.** Use the [review protocol](../research/methods/EVIDENCE_INTAKE_AND_REVIEW.md) before approved updates to `working/`.
