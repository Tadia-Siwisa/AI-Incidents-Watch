# Wide Search 2

`AI_Incident_Watch_WIDE_Search_2.xlsx` is a separate expanded discovery register current through 14 October 2026. It does not change the 46-family factual baseline or the dated evidence-update workbook.

## What it contains

The workbook contains 225 source records or candidate families:

| Source route | Rows |
|---|---:|
| Permission Protocol public incident-tracker dataset | 171 |
| METR documented-agent-incident register | 44 |
| Additional families researched directly in this pass | 10 |
| **Total** | **225** |

The broad routing is 84 reported, operational, or authorized-game records; 135 controlled evaluations or security demonstrations; and six screened METR cases that do not contain an identified task, permission, or system-boundary action. Thirteen rows are mapped to the existing baseline or dated backfill, including one possible overlap that still needs adjudication.

These totals are not an incident-prevalence estimate or a unique-event count. The imported trackers sometimes split campaigns into product, vulnerability, or run-level records, and different entries can describe the same underlying event. The `Relationship to existing corpus`, `Existing ID(s)`, and `Review status` columns make those limitations visible for later consolidation.

## Evidence state

The Permission Protocol source register linked 443 unique external URLs. An authorized HTTPS check opened 379; 64 returned access errors, paywalls, blocks, or missing pages. After adding direct sources found in this pass, 16 workbook rows still have no supporting source reachable from this environment. Those rows remain explicitly marked as unverified leads.

A reachable URL establishes that the route worked. It does not establish that every statement on the page is true. Permission Protocol classifications, severity labels, and authority-control fields remain identified as publisher analysis. METR rows retain METR's source quotations and original links but have not all received an independent run-by-run reconstruction in this pass.

The search also opened direct sources for high-value and disputed cases. Material corrections include:

- The DataTalks founder said he saw the `terraform destroy` command and did not stop it, does not blame Claude, and recovered the database after AWS restored an internal backup. This belongs in human-approved execution and process/configuration context.
- Amazon disputes that Kiro caused its service interruption, attributes the event to user error and a misconfigured role, and denies a claimed second AWS incident.
- AWS says malicious instructions reached Amazon Q extension version 1.84.0 but a syntax error prevented their execution and no customer environment was changed.
- EchoLeak was a working researcher proof of concept against Microsoft 365 Copilot. The reviewed research says Microsoft found no in-the-wild exploitation.
- The Gemini CLI advisory describes a critical remote-code-execution path in untrusted CI workspaces, not a confirmed exploited customer incident.
- Freysa released a real crypto prize, but this was the intended end condition of an authorized adversarial game.

## Workbook sheets

- `Read Me`: scope, counts, evidence warnings, and key corrections.
- `All Candidates`: all 225 rows, once each.
- `Reported & Operational`: reported real-world, internal operational, and authorized-game records.
- `Controlled & Security`: controlled evaluations, demonstrations, and vulnerabilities.
- `Existing Overlaps`: records reconciled to the baseline/update corpus or flagged as a possible duplicate.
- `Screened & Unreachable`: screened context plus rows whose linked supporting evidence could not be opened.
- `Source Registry`: 480 unique clickable URLs with access status and linked WS2 rows.
- `Search Log`: search routes, scope, result counts, and how results were used.

## Rebuilding

From the repository root:

```bash
python scripts/build_wide_search_2.py
```

The builder verifies the three source-collection counts, 225 unique WS2 IDs, workbook sheets, filter and frozen-header configuration, source coverage, and the generated workbook's ability to reopen with `openpyxl`. It also writes the machine-readable combined register to `data/wide_search_2/wide_search_2_register_2026-10-14.json`.

The dated raw search output is under `data/monitoring/raw/2026-10-14/`. Retrieved evidence and source-access results are under `evidence/wide_search_2/2026-10-14/`. The original three spreadsheets and every previously generated dataset remain unchanged.
