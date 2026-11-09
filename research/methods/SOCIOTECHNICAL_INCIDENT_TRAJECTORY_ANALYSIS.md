# Sociotechnical Incident Trajectory Analysis

**Project:** AI Agent Incident Watch  
**Methodology version:** Working v1, agreed in discussion 9 November 2026  
**Status:** Methodological plan approved for documentation; **case-level analysis using this framework has not yet been carried out or finalized**.  
**Research agenda:** [RESEARCH_AGENDA.md](../RESEARCH_AGENDA.md)  
**Research log:** [RESEARCH_LOG.md](../RESEARCH_LOG.md)

## 1. Purpose and framing

AI Agent Incident Watch investigates what documented AI-agent incidents, evaluations, demonstrations, and operational reports reveal about the relationships among **agent behavior**, **conditions and capabilities supplied by an operating environment**, **task and authorization boundaries**, **real-world reach**, **outcomes**, and **monitoring and reporting**.

The intent is not to reduce every source to a single action label or presume that every adverse outcome was an autonomous agent deviation. A reported action becomes analytically meaningful in relation to its assignment, triggering circumstances, available routes, applicable controls, affected systems, and the evidence that makes the account visible.

The study has several possible contributions: consolidating fragmented public evidence; describing observable capabilities and behaviors; distinguishing categories of risk and systems failures; identifying recurring conditions and pathways; examining the adequacy of detection and disclosures; and generating evidence-grounded defensive questions. **Defensive ideas and causal explanations are possible implications, not assumptions encoded into the data.**

### Working research question (retained from the 9 November agenda)

> Under what conditions, and through what mechanisms, do AI agents attempt or perform actions beyond their assigned tasks or authorized scope, and what happens when they do?

### Broader systems lens for synthesis (not a replacement for the formally logged question)

> What do documented AI-agent incidents reveal about the relationship between agent behavior, operating conditions, system boundaries, and consequential outcomes?

These two levels coexist: the first keeps authorization and scope deviations explicit; the second allows examination of system-level lessons even where no autonomous deviation is established. Any final change to the primary research question should be separately discussed and recorded.

## 2. Methodological approach

- **Sociotechnical systems perspective:** Agent, task, users/researchers/attackers, tools, permissions, platform architecture, external systems, and oversight constitute a coupled operating system.
- **Incident trajectory reconstruction:** Describe the observable sequence and interactions before assigning a pattern. Trajectories may branch, repeat, stop, or be only partially visible; do not force a linear story where the record does not support one.
- **Evidence-constrained process tracing:** Examine temporally ordered actions and possible mechanisms; do not infer a cause from chronology alone.
- **Comparative case analysis:** Compare reconstructed trajectories, including confirming cases and counterexamples, to derive recurring pathways and important differences.
- **Inductive synthesis:** Discover system-interaction patterns from the cases rather than imposing prior WHAT/HOW/WHERE or E01–E15 codes. Older exploratory taxonomies remain historical comparisons, not predetermined results.

### Unit distinctions

**The 188 reviewed entries are source records**, not 188 verified agent executions. A source may contain multiple runs or trajectories, and multiple sources may describe the same event. Where identifiable, link **source ID → case family → specific episode/run → action sequence**. Preserve unknown links without silently deduplicating or multiplying incidents.

A source with only an architectural vulnerability, a hypothetical exploit, a human-led operation, or an unsupported assertion still belongs in the evidence inventory, but **must not receive a fabricated agent trajectory**. Such records remain useful for the systems-risk and reporting analyses.

## 3. The nine incident-trajectory dimensions

These dimensions are a **consistent set of questions**, not nine mutually exclusive behavioral classes. For each dimension, record the supporting evidence, its limits, and whether it is unknown.

| # | Dimension | Core questions and what to capture |
| --- | --- | --- |
| **1** | **Task and authorization** | Who assigned what task? What was the intended objective, target, resources, and allowed/disallowed behavior? Distinguish explicit instructions, inferred intent, technical permission, and actual authorization. |
| **2** | **Operating environment** | Where did work begin: evaluation, simulation, authorized security demonstration, internal research, production, or another context? Which tools, credentials, APIs, system privileges, network access, sandbox and controls were actually available? |
| **3** | **Initiating conditions and direction** | What preceded the behavior: task failure, ambiguous target, external malicious instructions, researcher-designed stress, user request, infrastructure error, or unknown trigger? Was the particular action explicitly directed, externally redirected, selected by the agent as a method, or indistinguishable from available evidence? These origins may overlap. |
| **4** | **Observed action sequence** | What actions were attempted, blocked, completed or merely claimed, and in what supported order? Did the agent try alternatives, enlist another actor, persist, stop, or change course? Preserve intermediate steps and gaps. |
| **5** | **Mechanism or pathway** | Through which observed capabilities and routes was an action attempted or accomplished (e.g., tool call, token, interface, agent delegation, network route, external write)? Distinguish a documented technical mechanism from a proposed explanation. |
| **6** | **Boundary interaction** | Which task, authorization, target, trust, network, isolation, approval, or execution boundary was encountered? Was it respected, challenged, bypassed, crossed, or simply misconfigured by a person? An agent reaching a real system does **not** by itself prove a sandbox escape. |
| **7** | **System reach and affected environment** | Where did the action take place and what did it contact or change: isolated test asset, connected external service, real person, or live production resource? Keep **origin environment**, **reachable environment**, and **actually affected environment** separate. |
| **8** | **Outcome and consequences** | What resulted: refusal, containment, blocked attempt, completed operation, external contact, changes to data or systems, recovery, or unknown? Identify observed effects and reversibility without treating possibility or allegation as accomplished harm. |
| **9** | **Operational detection and response** | Who first observed the activity (agent operator, lab monitor, target organization, external researcher, user)? When was it detected, alerted, acknowledged, investigated, interrupted, contained, remediated or disclosed? Separate those milestones and unknown timestamps. |

### Crucial interpretive distinctions

1. **Induced versus agent-selected is not a binary.** Researchers can deliberately arrange an obstacle while the model selects a particular next action; attackers can introduce instructions; humans can direct AI systems in operations. Record both the source of the condition and the source of the specific direction, with uncertainty where appropriate.
2. **Technical reach is not authorization.** Having working credentials, a permissive API, or network access does not establish that the task authorized its use.
3. **External contact is not automatically containment escape.** An evaluation may permit normal internet access, contain an unintended live target, or genuinely have a restricted route circumvented. Investigate these mechanisms separately.
4. **Do not conflate attempted, demonstrated, completed, blocked, and alleged actions.** The same high-level verb can represent very different evidence.
5. **System behavior is broader than model action.** Identify configuration, design, permissions, human decisions, hostile content, or monitoring separately from choices actually attributable to the agent.

## 4. Separate, cross-cutting analysis: reporting and evidence visibility

**This is NOT a tenth incident-trajectory dimension.** It is an independent line of inquiry applied to all 188 sources and to the completeness of reconstructed trajectories.

Two kinds of visibility must remain distinct:

**A. Operational detection visibility (dimension 9):** What could operators, monitors, users, or affected organizations observe and respond to **while the activity occurred or afterward**?

**B. Public reporting / research visibility (this separate analysis):** What was actually documented or disclosed in a form the research can verify and reconstruct?

For every source, ask:

- Who made the disclosure (lab, evaluator, affected organization, independent security researcher, reporter, user), and when relative to the activity and discovery?
- Is the account based on first-party logs/transcripts, a detailed report, reproducible demonstration, a secondary summary, an allegation, or mixed evidence?
- Which of the nine trajectory dimensions can actually be established from the published evidence? Which are partially documented, contradictory, or unavailable?
- Are actor identity, assigned task, controls, authorization, exact routes, run counts, affected organizations, detection timestamps and containment actions disclosed?
- Are there independent confirmations, subsequent corrections, or conflicts between sources?
- How do public disclosure detail and missingness vary across the five evidence categories?

**Important boundary:** A sparse public report does not prove inadequate internal monitoring. Detailed retrospective logs do not prove real-time detection. Reporting completeness, organizational detection, disclosure incentives, and evidence reliability are different subjects.

This second analysis can itself yield substantive findings about blind spots, reporting asymmetry, research reproducibility, and which security questions are unanswerable with current public evidence.

## 5. Evidence corpus and preserved categories

**Frozen source-level analytical baseline:** the 188 reviewed source records, as classified in the 9 November 2026 audit.

| Primary evidence-source category | Records |
| --- | ---: |
| Security Demonstrations & Vulnerability Reports | 91 |
| Controlled Agent Evaluations | 48 |
| Reported Operational Events | 32 |
| Attacker-Directed AI Operations | 15 |
| Unclassified — No Supported Fit | 2 |
| **Total source records** | **188** |

Working inputs:
- [9 November full source category-fit review](../../data/working/2026-11-09/AI_Incident_Watch_188_Full_Category_Fit_Pass_2026-11-09.xlsx).
- [9 November 188-source plain-language reading file](../../data/working/2026-11-09/AI_Incident_Watch_188_Source_Reading_File_2026-11-09.xlsx).
- [30 October 188-source evidence-ledger snapshot](../../data/working/review_snapshot_2026-10-30/188_evidence_ledger.csv), retained as an earlier input, not the latest classification.
- [Historical factual rebuild of 46 case families](../../data/rebuilt/factual_rebuild.json), useful for evidence provenance and comparisons.

**These are five categories of evidence provenance/context, not five agent behavioral types.** Preserve source classifications during the initial trajectory reconstruction. An action's initiation, reach, and outcome can span categories. Do not reclassify sources in response to an interesting mechanism without separate review.

**Date boundary:** This fixed 188-source review is the analytical snapshot; incoming disclosures continue through the Incident Watch intake but do not silently change this study's denominator.

## 6. How we will conduct the next phase

### Stage 0 — Lock scope and evidence handling

- Use the reviewed **188 source IDs** and existing classifications without modifying them.
- Preserve source URLs, original narrative, review cautions, evidence strength, and any source-to-episode links.
- Define analytical outputs separately from the underlying dataset and original source captures.
- Log the analytical snapshot and the distinction between source, case family, run, and action.

### Stage 1 — Screen each source for reconstructable content

For each source, first establish **what kind of evidence it actually contains**:
- Observed agent action(s) — attempted or completed;
- induced/controlled action(s) (when demonstrated);
- agent-assisted or human-directed operation;
- vulnerability or potential pathway **without supported agent action**;
- source with incomplete, disputed, or unsupported claims.

The screening labels describe evidence availability. They must not be mistaken for proof of independent agent deviation or legal/ethical authorization.

### Stage 2 — Reconstruct incident trajectories when evidence permits

For an evidence-supported action, reconstruct the nine dimensions, keeping **observed fact**, **source attribution**, **evidence-based interpretation**, and **unknown** distinct.

Use a compact evidence record per trajectory with:
- Source ID, applicable case-family and run/episode links where known;
- each dimension's factual text, source locator and evidence status;
- explicit attempted/blocked/completed/alleged distinction;
- information on direction (agent-selected, externally induced, researcher/user/attacker instructed, mixed, or unclear);
- any alternative account or source contradiction.

Do not invent missing prompts, unobserved thought processes, permission rules, network boundaries, or detection timestamps. Multiple runs and branching routes may require more than one trajectory per source.

### Stage 3 — Pilot and discuss before broad coding

Reconstruct a **small contrasting sample** first (including, where available, a controlled evaluation that reached a live system, externally redirected agent behavior, a reported operational event, and a security vulnerability with no established agent action).

Bring the actual cases, known sequences, uncertainties and emerging distinctions **into the chat**. Discuss whether the nine dimensions capture the evidence and what needs refinement. **Do not update or recode the 188-source workbook, write final pattern labels, or advance to bulk coding without first discussing findings.**

The sample is a method test, not an early estimate of frequency.

### Stage 4 — Systematically reconstruct the frozen corpus

Once the method has been discussed, examine the source records within each of the five existing categories using the same nine questions. Preserve records with insufficient evidence rather than forcing trajectories. Track source coverage and gaps so all 188 have been screened even if only a subset supports action sequences.

Report descriptive findings in batches through the chat before modifying stored datasets or finalized coding. Do not allow ongoing intake to reset the fixed 188-source analysis.

### Stage 5 — Compare and induce system-level patterns

**After reviewing individual trajectories**, compare:
- recurring action pathways and alternative routes;
- different mechanisms leading to apparently similar outcomes;
- effects of authorization, tool access, network connectivity and environment configuration;
- differences between researcher-designed tests, induced redirection, ordinary operational tasks, and attacker-directed work;
- effective and ineffective boundaries, detection and containment;
- counterexamples and cases that resist proposed patterns.

Patterns should emerge inductively from evidenced relationships **across multiple dimensions**, not simply from the labels used for actions. Preserve non-exclusive pattern membership and exact source/episode mappings.

### Stage 6 — Analyze reporting separately

Cross-tab evidence coverage by dimension and by source-evidence category. Examine detection and disclosure time separately when possible. Identify specific missing information that prevents reconstruction or interpretation. Describe the limits of conclusions; do not treat unavailable public evidence as evidence that an event did not occur.

### Stage 7 — Synthesize and discuss the findings

Present conclusions in three distinct levels:

1. **What the collected evidence establishes:** traceable actions, conditions, system interactions, observed outcomes, timing, and reporting limits.
2. **What the evidence suggests:** plausible cross-case relationships and defensive hypotheses, with counterexamples and uncertainty.
3. **What remains unknown or should be tested:** missing telemetry, experimental comparisons, unanswered control questions, and promising directions for future research.

Possible practical implications include evaluation isolation, permission design, action-level monitoring, detection/response, evidence retention, and disclosure standards, but **do not prescribe a solution as a settled finding**.

### Stage 8 — Decision, publication and next research cycle

Review synthesized findings **with the researcher in chat before applying analytical changes**, deciding whether to refine the framework, conduct targeted source verification, request more evidence, publish a report, or begin a new analysis. Only approved decisions alter classification, permanent analytical tables, or published outputs.

**Completion criterion for this snapshot:** All 188 sources screened; evidence-supported trajectories reconstructed to the extent possible; reporting/missingness analyzed; recurring system-interaction patterns compared with counterexamples; conclusions separated into established, suggested and unknown; research discussion held. This does **not** require resolving every unknown or waiting for all future incidents.

## 7. Safeguards for counts and conclusions

- **Denominator:** counts of *sources* must be labeled as sources. When available, report deduplicated cases/runs separately. Never count targets, actions, screenshots, or affected people as independent incidents.
- **Multi-label findings:** one trajectory can involve multiple pathways and boundaries; category totals need not sum to 188.
- **Nonrepresentative collection:** sampled disclosures and security studies cannot yield general incident prevalence, provider safety rates, or trends without exposure denominators.
- **Causal claims:** reconstructing an event sequence does not prove the model's internal intent or that one factor caused an effect. Identify rival explanations when plausible.
- **Evidence traceability:** every consequential finding must link back to source IDs and disclosed evidence. Keep uncertainty, corrections, contradictory reports, and missing data visible.
- **No premature dataset edits:** during the present discussion-led phase, share findings first. Documentation of this agreed plan is authorized; changes to source rows, action codes and conclusions are not.

## 8. Immediate next action

**Pilot the nine-dimension trajectory reconstruction on contrasting evidence records**, beginning with the controlled-evaluation-to-real-system example discussed, then examining dissimilar cases. Share the reconstructed trajectories and the separate reporting assessment in chat for critical discussion **before any new analytical coding or corpus modifications**.
