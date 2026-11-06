# 188-source split — working review, 2026-11-06

## Scope and counting unit

This directory contains a COMPLETE **source-record-level** disposition of the evidence-reviewed 188-row ledger dated 2026-10-30. Every original source ID appears exactly once in `source_dispositions_188.csv`. The source ledger and the pre-existing 10-row `individual_incidents.csv` draft are preserved unmodified; this work remains on branch `analysis/incident-normalization-2026-11-06` rather than the canonical main dataset.

**Important:** 188 refers to source records, not independent real-world incidents. The split below is complete **as classification of all 188 sources**, but a fully validated unique incident/run count is *not* established. We have not yet reconstructed every publication from its underlying execution transcripts or de-duplicated all 46 legacy case families against one another. Please do not describe the 101 agent-action sources as "101 incidents."

## Reviewed grouping (counts of source records)

| Track | Sources | Interpretation |
|---|---:|---|
| AGENT_ACTION | 101 | Reported, evaluated, or attacker-induced agent behavior; some are aggregated or weakly evidenced |
| VULNERABILITY | 58 | Software, infrastructure, integration, access-control or sandbox exposures, sometimes demonstrated; no *independent* agent deviation necessarily |
| HUMAN_LED | 15 | Human-controlled offensive cyberattack, agent-assisted campaigns, or compromise of agent service |
| RESEARCHER_LED | 3 | Researcher-scoped offensive tests, which must not be conflated with model-initiated deviations |
| EVIDENCE_HOLD | 9 | Inadequate corroboration, unresolved causal attribution, or activity where model behavior has not been established |
| GOVERNANCE | 1 | Commercial service access or authorization dispute |
| OUT_OF_SCOPE | 1 | Conventional application vulnerability with no supported AI-specific causal nexus |
| **TOTAL** | **188** | Exactly one assigned track per original source ID |

These working group choices include substantive changes from the earlier eligibility overlay (115 / 45 / 14 / 3 / 7 / 3 / 1). For example, we have reclassified sources about exposed agent controllers, agent impersonation, sandbox implementation bugs and token theft as vulnerabilities even when the earlier record suggested agent action. Those judgment calls need case-specific technical review before final publication. Likewise human exploitation of METR's exposed research agent interface (PP-141) is not autonomous AI theft.

## Files

- `source_dispositions_188.csv`: **canonical mapping for this draft**, 188 rows, source references, working classifications and caveats.
- `agent_actions_sources.csv`, `vulnerability_sources.csv`, `human_led_attack_sources.csv`, `researcher_holds_context_sources.csv`: four mutually exclusive filtered views (101 + 58 + 15 + 14 = 188).
- `agent_case_family_index_101.csv`: one line per *agent-action source* with traceable reference, original observed statement, affected environment and candidate family key. These are **not** all verified distinct incidents.
- `documented_aggregate_splits.csv`: 24 family/run/experiment notes. These are **nested explanatory records**, not 24 additional incidents. It contains four Anthropic family labels (the four documented incidents across seven runs), known Opus 4.7 run members, and ten AISI run placeholders. Some entries overlap in parent/child relationship; **never sum them**.
- `individual_incidents.csv`: **pre-existing 10-entry pilot**; not superseded by or equal to the 188 classification.
- `../review_snapshot_2026-10-30/188_evidence_ledger.csv`: immutable source evidence ledger used as source of truth.

## Deduplication and case-family crosswalk

Records already related to the older 46-case factual rebuild have been given links, notably PP-165 → N01 (Replit, *duplicate*, not new), PP-125 → N05, PP-046 → N04, PP-086 → N12, PP-071 → N14, PP-063 → N02/N06/N07/N08, PP-056 → N15, PP-019 → N09 (weak primary link), PP-018 → N17, PP-011 → W06, PP-054 → W21. These are **provisional cross-references**, not proof that other source rows lack duplicates.

### Especially important multi-unit source records

- **PP-063:** Four Anthropic research incident **families** (N02, N06, N07, N08), spanning seven reported runs. Four Opus 4.7 runs involved the *same family*. Do not count the family crosswalk and seven runs twice.
- **PP-056:** UK AISI describes **one evaluation cluster**, 122 total runs, 10 runs with unsanctioned behavior, **19 actions**, mostly linked to one sustained sequence. These are not 19 independent incidents. Source: https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing
- **PP-076:** Four reported successful payment-trigger tests among 26 model tests. The source ledger does not supply four individually attributable traces; retain experiment totals rather than inventing separate case identities.
- **MAN-006**, **PP-055**, **PP-042:** Multi-product security experiments. Their individual examples may be distinct *scenarios*, but not automatically separate operational incidents.
- **PP-071:** The Hugging Face/ExploitGym research episode involved multiple contacts, tools, and model runs; one publication or many actions cannot be assumed to equal one model-run incident. A granular timeline is still required.
- **MAN-001/MAN-002/MAN-004/PP-009/PP-157:** Aggregate publications or bundled advisories with unresolved internal unit counts.

## How to review

1. Review `source_dispositions_188.csv` for classifications and justified holds. Keep the original evidence file unchanged.
2. Use `agent_case_family_index_101.csv` to examine reported agent behavior. Separate **unprompted deviation**, **attacker-induced action**, **research evaluation**, and ordinary task outcome before analysis.
3. Use `documented_aggregate_splits.csv` for known family/run structure; do **not** count parent and child rows together.
4. To publish a true *unique incidents* total, check actual original publication/transcript per candidate, resolve duplicate event IDs, identify specific task and authorized scope, bind actual actions to each affected environment, distinguish completed from attempted and hypothetical effects, and only then assign stable incident IDs.

## Status

**Finished:** full 188-source partition and saved GitHub branch; evidence pointers retained; major known multi-unit cases flagged and partially split.

**Not claimed finished:** all underlying 188 records individually independently verified as distinct real-world incidents; exhaustive run-level reconstruction of aggregate studies; cross-source deduplication against all 46 old case families; weekly intake and canonical main update.

This is deliberately conservative: incomplete public reporting remains visibly incomplete instead of being silently filled in.
