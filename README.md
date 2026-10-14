# AI Incidents Watch

Evidence rebuild of the narrow, wider, and Reddit incident registers supplied on 9 October 2026.

The first factual-review pass is complete. All 63 input rows are preserved and mapped to 46 deduplicated case families. Each family now has an evidence finding, supported facts, corrections or unresolved claims, source provenance, and explicit analysis flags.

Do not use the imported workbook claims as facts. Use `data/rebuilt/factual_rebuild.json` or its CSV export. The import layer intentionally preserves the workbooks verbatim; the factual layer records what the retrieved evidence supports.

## Results as of 9 October 2026

| Claim finding | Cases |
|---|---:|
| Supported | 21 |
| Partly supported | 19 |
| Contradicted | 2 |
| Insufficient evidence | 3 |
| Not an incident | 1 |
| **Total canonical families** | **46** |

Fifteen families meet the strict `include_confirmed` threshold. Six are retained with material qualifications, five as controlled-evaluation context, three as product/configuration context, fourteen remain unverified Reddit leads, two core claims are rejected, and one is a question rather than an incident.

These counts describe evidence status, not incident prevalence or severity. Aggregate observations such as three target companies, 19 actions, 53 images, or 15 affected scanner systems are kept inside their incident families and are not automatically counted as separate incidents.

## Repository layout

- `data/original/`: byte-preserved copies of the three supplied spreadsheets.
- `data/rebuilt/original_manifest.json`: original file sizes and SHA-256 hashes.
- `data/rebuilt/workbook_inventory.json`: every workbook cell and hyperlink, including documentation sheets. Workbook text is source material, not project instructions.
- `data/rebuilt/records.json`: the 63 imported rows with workbook and row provenance. This is the unchanged assertion layer.
- `data/rebuilt/claims.json`: 908 imported field-level assertions. These are not automatically verified.
- `data/rebuilt/factual_rebuild.json`: authoritative case-level factual findings and analysis flags.
- `data/rebuilt/factual_rebuild.csv`: flat export for spreadsheet and analysis tools.
- `data/rebuilt/factual_claims.json` and `.csv`: case findings, supported facts, and correction/unresolved statements as analysis-ready claim rows.
- `data/rebuilt/factual_sources.json`: source URLs, evidence tiers, local copies, locators, limitations, byte counts, and SHA-256 hashes.
- `evidence/cases/`: one readable evidence report for each canonical family.
- `evidence/text/`: text conversions of supplied sources.
- `evidence/researched/`: additional primary, vendor, and independent sources found during web research.
- `evidence/reddit/`: direct Reddit embed snapshots, extracted text, user-posted images, and third-party archived comments.
- `VERIFICATION.md`: methodology, evidence rules, major corrections, and remaining gaps.

## Evidence access

No browser/search connector was installed in the environment. The environment's enforced network profile permitted unrestricted outbound HTTP, so research used that authorized route. Supplied URLs were opened directly; targeted discovery used DuckDuckGo's HTML search endpoint, followed by direct retrieval of the relevant primary or independent pages.

Direct Reddit pages triggered anti-bot handling. The public Reddit embed endpoint provided the original post content and timestamp for 19 cited posts. PullPush supplied archived comments and is identified as a third-party archive in every citation. R007 had no URL. Images linked from R003 and R017 were preserved; they remain user-supplied artifacts whose provenance cannot be independently proved.

## Material corrections

- R014's production-database deletion allegation is contradicted in-thread by a Replit representative, who said the database and data were still present. The workbook's separate “no write access” assertion was not found.
- R016 was a Replit platform incident that inserted an unintended `DATABASE_URL` secret into some projects. The author said no data was lost; the evidence does not support agent causation.
- N17's primary source says the run ended at 12:34:30, not the workbook's 10:08:22. Detection was rapid, while termination occurred about 2.5 hours after the automated alert.
- N09's three-company event is supported by Google and Irregular statements reported by independent outlets. No source was found for the workbook's additional “sworn confirmation Oct 5” claim.
- N06-N08 occurred from April onward; exact incident dates were not disclosed. The workbook's separate May dates are unsupported.
- W01 requires the GPT-4 System Card. The supplied `gpt-4.pdf` technical report does not contain the TaskRabbit passage.
- W05 was a controlled demonstration with dummy data, and Supabase said no customer incident was reported. The originally supplied product-documentation URL did not substantiate the demonstration.
- W06 confirms 53 user-provided images posted to image hosts, but does not disclose the workbook's claimed October 2025-January 2026 period. Fifty-three is an image count, not an incident count.
- N15's 19 unsanctioned actions were unsuccessful attempts in a deliberately internet-enabled evaluation; AISI reported no real-world harm. It is routed to the wider set.

## Rebuilding generated files

From the repository root:

```bash
python scripts/build_factual_rebuild.py
```

The script checks that every canonical candidate is covered, regenerates the JSON/CSV factual layer and all 46 case reports, hashes every cited local source, and prints summary counts.

`python scripts/rebuild_register.py` regenerates the raw import layer from the workbook inventory. It does not change the originals. Run the factual rebuild afterward if the import layer changes.

## Exploratory analysis

The evidence-aware research report is in
[`reports/AI_Agent_Incident_Exploratory_Analysis.md`](reports/AI_Agent_Incident_Exploratory_Analysis.md).
The formatted PDF edition is available at
[`reports/AI_Agent_Incident_Exploratory_Analysis.pdf`](reports/AI_Agent_Incident_Exploratory_Analysis.pdf).
It analyzes the full 46-family collection, the 26-family wider supported set,
and the 15-family higher-confidence set separately. The report includes the
dataset audit, evidence assessment, descriptive and exploratory results,
detection/response reconstruction, system-level findings, hypotheses,
unknowns, implications, and recommendations.

The reproducible case coding and aggregate tables are under `analysis/`. To
regenerate the coding, tables, and figures:

```bash
python scripts/analyze_incidents.py
```

The script checks that every factual case family is represented exactly once.

## Evidence updates after the baseline

The dated delta register is [`AI_Incident_Watch_Evidence_Updates.xlsx`](AI_Incident_Watch_Evidence_Updates.xlsx). It keeps new reports, updates to existing cases, pre-baseline evidence found later, screened candidates, and a one-row-per-family watch log separate from the 46-row master workbook.

The first delta scan is current through 13 October 2026. It contains 13 provisional new families, two updates affecting existing cases, three backfills, four screened candidates, and direct links to 18 preserved sources. These are review buckets rather than additions to the confirmed-incident count.

See [`EVIDENCE_RADAR.md`](EVIDENCE_RADAR.md) for the findings, evidence rules, repeatable scan commands, and notification limits. Rebuild the update workbook with:

```bash
python scripts/build_evidence_updates.py
```

Run the next discovery-only scan with:

```bash
python scripts/scan_evidence_radar.py
```

## Wide Search 2

The separate expanded discovery workbook is
[`AI_Incident_Watch_WIDE_Search_2.xlsx`](AI_Incident_Watch_WIDE_Search_2.xlsx).
It contains 225 source records or candidate families: 171 from Permission
Protocol's public source register, 44 from METR's documented-agent-incident
register, and ten additional directly researched families. Reported events,
controlled tests, existing-corpus overlaps, screened cases, and unreachable
source leads remain visibly separated. This is a discovery register, not a
confirmed-incident count or unique-event census.

See [`WIDE_SEARCH_2.md`](WIDE_SEARCH_2.md) for counts, source-access results,
material corrections, limitations, and sheet definitions. Rebuild the workbook
and combined machine-readable register with:

```bash
python scripts/build_wide_search_2.py
```
