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
