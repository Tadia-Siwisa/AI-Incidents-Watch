# AI Agent Incident Watch

**Independent, evidence-led research into AI agents' actions, task scope, authorization and the systems they can affect.**

## Current working research question

> **Under what conditions, and through what mechanisms, do AI agents attempt or perform actions beyond their assigned tasks or authorized scope, and what happens when they do?**

The study starts with **what an agent was observed attempting or doing**. We then examine the assigned task, technical access, authorization, environmental conditions, sequence of actions, real-world reach and observed outcomes. A reported vulnerability or security test is not automatically a confirmed unauthorized autonomous action.

[Research agenda](research/RESEARCH_AGENDA.md) · [Dated research log](research/RESEARCH_LOG.md)

## Published research

**First authored report — 6 October 2026:** **[Artificial Actors in Real-World Systems](reports/published/Artificial_Actors_in_Real_World_Systems_2026-10-06_TEXT.md)**, by Tadia Siwisa. This is an **extracted-text reading edition** of the author's 14-page illustrated PDF. The original PDF's figures and design are **not** reproduced here; the PDF is not yet uploaded to GitHub. The report describes a selected set of **17 incidents** with a broader annex.

The longer **13 October Codex-generated exploratory analysis** is *not* an approved second report. It is retained for transparency as a [historical working draft](archive/reports/codex_exploratory_2026-10-13/).

## Data and research stages

| Stage | Records | What is counted |
| --- | ---: | --- |
| Original factual reconciliation | **46 case families** | Reconciled from **63 imported rows**, reviewed in October |
| Expanded Wide Search 2 | **225 candidate/source records** | Broad discovery pool, not confirmed incidents |
| Selected evidence-review corpus | **188 source records** | Working sources; not 188 distinct agent executions |
| Current category review (9 November 2026) | **188 source records** | [Five-category classification audit](data/working/2026-11-09/AI_Incident_Watch_188_Full_Category_Fit_Pass_2026-11-09.xlsx), with a separate [reading file](data/working/2026-11-09/AI_Incident_Watch_188_Source_Reading_File_2026-11-09.xlsx) |

**Current evidence-source categories (9 November review):**

| Evidence source category | Records |
| --- | ---: |
| Security demonstrations and vulnerability reports | 91 |
| Controlled agent evaluations | 48 |
| Reported operational events | 32 |
| Attacker-directed AI operations | 15 |
| Unclassified / insufficient supported fit | 2 |
| **Total** | **188** |

**First broad conclusion:** 139 of 188 sources (73.9%) describe security demonstrations, vulnerability research or controlled evaluations. This is the makeup of the *collected evidence*, not the prevalence of agent failures in the world. Source type and affected environment are separate dimensions: a research evaluation may contact a real system.

**Version clarification:** The repository contains the [30 October 188-source evidence ledger](data/working/review_snapshot_2026-10-30/188_evidence_ledger.csv). The [9 November classification audit](data/working/2026-11-09/AI_Incident_Watch_188_Full_Category_Fit_Pass_2026-11-09.xlsx) and [188-source reading workbook](data/working/2026-11-09/AI_Incident_Watch_188_Source_Reading_File_2026-11-09.xlsx) are now synchronized here. The October 30 evidence ledger remains a historical input snapshot, not the current reviewed classification.

## Research process

**Collect → verify → reconcile → classify the evidence → identify observed actions → derive behavioral groups → study scope, conditions, mechanisms and consequences.**

The current phase is **inductive extraction and grouping of attempted/completed agent actions within the five source categories**, followed by counts of how often each behavior group appears. Agent actions are the focus; outcome and whether the behavior reached a real system will be coded separately. No new action-group results have yet been finalized.

## Find your way around the repository

| Folder | Purpose |
| --- | --- |
| **[reports/](reports/README.md)** | Authored research designated for publication |
| **[research/](research/README.md)** | Working questions, decisions, logs, process documentation and navigation |
| **[data/](data/README.md)** | Current source ledger, historical workbooks, discovery and intake datasets |
| **[evidence/](evidence/README.md)** | Retrieved sources, case notes and supporting records |
| **[analysis/](analysis/README.md)** | Historical 46-family analysis coding, tables and statistics |
| **[scripts/](scripts/README.md)** | Reproducible research and intake tools |
| **[archive/](archive/README.md)** | Historical or unapproved drafts, not presented as publications |

The hidden `.github/` directory holds automation, including incident-intake workflow.

**Research caution:** The study is disclosure-limited, and many cases lack complete tool traces or authorization details. Distinguish sources, distinct runs, case families and affected objects; never interpret raw counts as vendor/model failure rates.

**Next:** study the observed AI-agent behaviors in each source-evidence group, without imposing predetermined behavior categories.
