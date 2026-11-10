# AI Agent Incident Watch — Research log

**Purpose:** Persistent, chronological record of research decisions, analyses, changes, limitations, findings, and next actions. This is separate from the datasets and should be updated after each substantive research session.

**Rules**
- Add new dated entries; do not silently rewrite earlier findings. Record corrections explicitly.
- Distinguish **completed work**, **working hypotheses**, **decisions**, **limitations**, and **pending work**.
- Cite the relevant source ID, repository path, or artifact when possible.
- Keep source-record, unique-episode, and case-family denominators separate.
- Do not treat research findings as confirmed production incidents without supporting evidence.

---

## 2026-11-09 — Source-evidence categories finalized (working classification baseline)

**Work completed**
- Revisited the question of what evidence the 188-record historical corpus contains, separately from the later question of which events constitute individual agent incidents.
- Established four substantive primary source-evidence categories and one exception category:
  - Security Demonstrations & Vulnerability Reports: **91** source records.
  - Controlled Agent Evaluations: **48**.
  - Reported Operational Events: **32**.
  - Attacker-Directed AI Operations: **15**.
  - Unclassified — No Supported Fit: **2**.
  - **Total: 188 source records.**
- Retired Reporting Reliability as a primary source-evidence category; retained it as a cross-cutting observable behavior.
- Performed a category-fit desk pass across 188 preserved source IDs, referring to existing ledgers, reconciliations, and reading descriptions. Changes were documented in the separate working audit workbook.
- Preserved the original source descriptions and prior labels. The 188 records are **not** 188 independently verified incident executions.

**Examples informing classification**
- **PP-142 (CodeWall/McKinsey Lilli):** Security demonstration / vulnerability report. A security researcher using an AI agent reached a production service; the source's purpose was to demonstrate a weakness, not evaluate the agent's capabilities. Permission to test in advance was not independently established.
- **PP-070 (Elastic / coding-agent network activity):** Reported operational event; suspicious-looking connections and persistent background processes were observed, but whether they were authorized or malicious was unresolved. Ambiguous intent does not alone make the *evidence category* unclassifiable.
- **PP-011 and PP-071:** Retain the distinction between research tasks/evaluations and the real systems an agent might contact. Source IDs and episode mapping must be respected; do not equate research-to-real contact with a demonstrated sandbox escape.
- **PP-101 and PP-116:** Placed in Unclassified for lack of a supported fit, not simply for unknown motive.

**Primary evidence-landscape observation**
- **139 of 188 source records (73.9%)** come from security demonstrations/vulnerability reports or controlled agent evaluations (91 + 48).
- The collected evidence therefore gives relatively strong visibility into deliberately investigated weaknesses and test behavior, but **cannot establish how often agents deviate in ordinary deployment**.
- Evidence provenance and affected environment are separate dimensions. A research-origin record may still involve a real production system.

**Limits**
- The category-fit review reused previously validated evidence and descriptions; it was not a fresh reread of all 188 external source URLs.
- Counts describe the **collected source mix**, not a rate of AI incidents, victims, or successful breaches.
- The current category audit workbook was generated in the ChatGPT file workspace/library, **not committed to this GitHub repository** as part of the original classification pass.

## 2026-11-09 — Primary research question and next analytical phase

**Working research question**
> Under what conditions, and through what mechanisms, do AI agents attempt or perform actions beyond their assigned tasks or authorized scope, and what happens when they do?

**Working definition**
An out-of-scope action is an AI agent's attempted or completed action beyond its assigned task, authorized permissions, or established operating boundaries, **where the available evidence supports the mismatch**. Unintended, surprising, or harmful behavior is not automatically proven out of scope.

**Research decision**
- **Start with observable agent actions**, not predetermined categories of failure.
- Examine each source within its existing source-evidence category. Describe actions attempted or completed, and separately mark records that only demonstrate vulnerabilities, proposed actions, or human-directed AI assistance.
- Derive recurring *behavior groups inductively* from the observed actions; allow overlapping groups; count source records per group **within each source category**, and track episode/case-family counts separately when possible.
- **Only after that** evaluate authorization mismatch, conditions, mechanisms, environment of origin versus reached/affected systems, results, detection, and containment.
- Do not assume every record demonstrates autonomous agent behavior or an out-of-scope action.

**Current status:** Research agenda documented; no new inductive behavior-group findings or counts have yet been produced under this newly agreed phase.

**Next action:** Begin record-level action extraction within the five locked source-evidence categories, induce behavior groups, then compute category-level and cross-category descriptive counts.

## 2026-11-09 — Documentation organization

**Decision:** Research log and research agenda must be standalone version-controlled Markdown files in `research/`, not worksheets embedded in the incident dataset.

**Change:** Created this persistent research documentation area and a navigation index to existing reports and scripts. Existing `data/`, `analysis/`, `reports/`, `scripts/`, and `docs/` repository contents are not relocated or overwritten by this change.

**Outstanding housekeeping:** Some newer working Excel audit and reading artifacts are available in the ChatGPT library rather than the repository; any future repository migration should preserve filenames, provenance and version dates.

## 2026-11-09 — Repository cleanup and publication distinction

**Decision:** The root README becomes the main project navigation page. Historical October workbooks are retained under `data/history/2026-10/` (same bytes, unchanged original file names). Supporting verification and collection documents now live under `research/methods/`. Raw evidence stays in `evidence/` and historical derived analysis in `analysis/`.

**Publication status:** The author's 6 October 2026 *Artificial Actors in Real-World Systems* is the first authored research report. A GitHub text-only reading edition was extracted from its 14-page PDF; the original designed PDF has not yet been committed. The 13 October Codex exploratory report and its PDF/figures are **working drafts**, now archived rather than listed as official publications.

**Reproducibility:** Historical Python build paths were updated to their moved workbook and draft-report locations; source-linked case evidence was not deleted. The substantive source records and counts were not changed as part of cleanup.

**Pending:** Synchronize the newer November 188-source classification and reading workbooks into `data/working/` and add the original published PDF when binary-file upload is available. The active analysis remains observed agent actions, their inductive behavior groups and counts.

## 2026-11-09 — Current 188-source workbooks synchronized

**Action completed:** Uploaded the original Excel files unchanged into `data/working/2026-11-09/`: `AI_Incident_Watch_188_Full_Category_Fit_Pass_2026-11-09.xlsx` (six sheets, 188-review-row worksheet) and `AI_Incident_Watch_188_Source_Reading_File_2026-11-09.xlsx` (six sheets, 188-source reading list and index). Verified both workbooks as valid ZIP/Open XML packages and checked their Git blob hashes match the originals. Updated repository navigation links.

**Scope:** No recoding, changes to classifications, new incident claims, or alteration of source descriptions was performed during this synchronization. October 30 ledger remains a prior dated evidence snapshot. The separate November 7 source-to-episode reconciliation is not part of this two-file upload.

**Next action:** Begin the agreed behavior-first inductive review using the current 188-source classification and reading workbook.

## 2026-11-09 — Agreed sociotechnical incident trajectory methodology

**Decision:** Examine AI-agent incidents as sociotechnical system interactions, reconstructing evidence-supported incident trajectories rather than categorizing isolated actions. The original scope-and-authorization research question remains recorded; a broader systems question guides synthesis.

**Documented protocol:** [Sociotechnical Incident Trajectory Analysis](methods/SOCIOTECHNICAL_INCIDENT_TRAJECTORY_ANALYSIS.md).

**Nine incident-trajectory dimensions:** (1) Task and authorization, (2) operating environment, (3) initiating conditions and direction, (4) observed action sequence, (5) mechanism or pathway, (6) boundary interaction, (7) system reach and affected environment, (8) outcome and consequences, and (9) operational detection and response.

**Separate research inquiry:** Public **reporting and evidence visibility** is cross-cutting, not a tenth trajectory dimension. Examine completeness, published source support, corrections and omissions across all 188 source records. Absence of public detail does not establish ineffective operational monitoring.

**Plan:** Keep 188 November-reviewed sources and five existing evidence categories fixed. Begin with a pilot of contrasting documented cases (controlled research reaching real systems, externally redirected agent behavior, operational events, and vulnerability-only evidence). Reconstruct the nine dimensions where supported and discuss case findings **in chat before changing any dataset, settled coding, or analytical output**. Then undertake full-source screening, comparative trajectory analysis, separate reporting analysis and synthesis into established findings, evidence-supported suggestions and unresolved questions.

**Current status:** Methodology agreed and documented; no new trajectory reconstructions or counts finalized. No source files or datasets edited.

**Next action:** Present contrasting-case pilot with evidence gaps and alternative explanations for research discussion.

## 2026-11-10 — Two-stage automated report intake

**Question addressed:** How can daily AI Frontier Watch and AI Agent Incident Watch disclosures be captured without losing updates or quietly changing reviewed research?

**Implementation:** Added an owner-authored `[Evidence]` issue template, separate GitHub Actions staging workflow, canonical `data/intake/incoming_evidence.json`, and automatically generated `data/intake/incoming_evidence.xlsx`. Existing `[Incident]` lead intake remains separate and unchanged. Intake records retain source URL, dates, related case, changes, uncertainty, source channel and review status. Potential duplicate disclosures are flagged. Only the intake JSON/XLSX are eligible for automatic GitHub Actions commits.

**Live integration test:** The 6 November WorkOS/ARTEX disclosure was submitted as [GitHub evidence issue #5](https://github.com/Tadia-Siwisa/AI-Incidents-Watch/issues/5), automatically staged as **EV-00005** with `Pending review` status, and rendered in the incoming evidence workbook. The submission is an **update to an existing case**, not a new confirmed source-case record.

**Scheduled reporting:** Updated the existing daily AI Agent Incident Watch and AI Frontier Watch task instructions to check for prior `[Evidence]` issues, create structured evidence-intake issues for substantive updates using connected GitHub access, and label any GitHub handoff failure `NOT STAGED`. There is no extra monitoring task.

**Review boundary:** Working classification and reading workbooks were **not** updated. Promotion requires explicit discussion and researcher approval; the approved change and supporting evidence should be logged here. Current implementation supports Stage 2 as a supervised research workflow rather than an unattended workbook-writing bot.

**Next:** Review WorkOS EV-00005 and compare recent disclosures to the queue for historical backfill. Confirm the scheduled tasks can create GitHub issues from their own execution context on their next normal run.


## 2026-11-10 — Backfill of missed disclosures from 27 October

**Period screened:** 27 October–10 November 2026, plus earlier incidents receiving materially new disclosures in that period. This is an initial targeted backfill, not a guarantee of exhaustive coverage.

**Actions completed:** Compared the October 30 repository source ledger, pre-existing 28 October intake/reconciliation notes, and the separate incoming-evidence register. Searched for official disclosures and credible reporting, then added 11 `[Evidence]` intake issues (#6–#16), in addition to the already staged WorkOS update (#5). All 12 are recorded as **Pending review** in `data/intake/incoming_evidence.json` and its generated Excel workbook. Existing incidents and the 188-source reviewed dataset were not changed.

**Source types covered:** Existing-incident updates (OpenAI monitoring, Chainalysis revisions, Australian Medicare review), reported operational events (WorkOS, disputed Pentagon/Claude Code report, Railway/Primcloud), attacker-directed AI use (two distinct Microsoft research items), product/security vulnerabilities (Apiiro coding-agent settings), and screened adjacent infrastructure incidents (Binance, NEAR AI, Mittwald). These are incoming *evidence records*, not 12 newly confirmed incidents. Some are likely contextual rather than eligible for a strict autonomous-deviation cohort.

**Pipeline reliability correction:** In a burst of issue submissions the initial Actions trigger did not reliably capture every issue in the JSON/XLSX register. Changed `scripts/update_evidence_intake.py` to reconcile all owner-authored `[Evidence]` issues on every run using the GitHub read-only issue API; the GitHub Action now supplies the scoped `GITHUB_TOKEN`. Reconciliation recovered all 12 issues. Future issue creation should not depend on a single event being delivered or run to completion.

**Outstanding work:** Compare the 12 entries with all current case/episode family mappings, verify source details and caveats, and discuss dispositions before approving any promotion. Consider additional targeted search of incident-watch reports and source trackers for potential omissions; the backfill is preliminary. Do not count one report, one campaign, or one victim as one autonomous AI-agent incident.

**Next action:** In the research chat, start with major evidence-changing updates (WorkOS and Chainalysis) and research-environment-to-real-system cases, then review human-directed operations and contextual records separately.

---

## Template for future entries

### YYYY-MM-DD — [Short session title]
**Question addressed:**  
**Evidence and files consulted:**  
**Actions completed:**  
**Findings (with counts and denominators):**  
**Decisions and definitions:**  
**Limitations / unresolved questions:**  
**Changes to datasets/scripts/reports:**  
**Next action:**
