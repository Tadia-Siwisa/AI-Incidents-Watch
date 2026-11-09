# AI Agent Incident Watch — Working research agenda

*Initial research question agreed 9 November 2026; methodological expansion agreed later that day. This is a working agenda, not completed findings. See the [research log](RESEARCH_LOG.md) and the [agreed trajectory-analysis methodology](methods/SOCIOTECHNICAL_INCIDENT_TRAJECTORY_ANALYSIS.md).*

## Primary research question

> **Under what conditions, and through what mechanisms, do AI agents attempt or perform actions beyond their assigned tasks or authorized scope, and what happens when they do?**

## Broader sociotechnical systems framing (agreed 9 November)

> What do documented AI-agent incidents reveal about the relationship between agent behavior, operating conditions, system boundaries, and consequential outcomes?

This is the **broader interpretive lens**, not an unapproved replacement for the working research question above. The investigation now uses [Sociotechnical Incident Trajectory Analysis](methods/SOCIOTECHNICAL_INCIDENT_TRAJECTORY_ANALYSIS.md): nine dimensions to reconstruct the task/environment → initiating conditions → action sequence → mechanism → boundary → reach → outcome → detection and response.

**Reporting and evidence visibility is a separate cross-cutting analysis**, examining public disclosure detail, evidence reliability and missingness across every trajectory and evidence category. Do not conflate incomplete public reporting with failure of real-time operational detection.

**First phase:** Screen and reconstruct a small, contrasting sample, then **discuss all case findings in chat before changing the dataset or extending to bulk coding**. Follow up by comparing full-corpus trajectories and emergent system-interaction patterns; action labels alone do not define the final taxonomy. The full dated protocol is in the linked methodology document.

## First principle: behavior before explanation

First establish **what an agent actually attempted or did**. Then examine the **documented assignment and boundary**, **conditions**, **observable sequence**, and **outcome**. A security vulnerability or a human's use of AI is not automatically an independent agent action.

### Supporting questions

| ID | Question | Status |
| --- | --- | --- |
| SQ1 — Actions | What concrete actions did agents attempt or complete within each source-evidence category? Was agent action observed, or was the source a vulnerability, a hypothetical path, or AI assistance? | **Next** |
| SQ2 — Inductive patterns | Which recurring action and behavior groups emerge **from the evidence**, and how many source records exhibit each group within and across categories? | **Next** |
| SQ3 — Scope | Which actions demonstrably exceeded assigned tasks, permissions, or boundaries? Which are potentially out of scope, within scope, or indeterminate? | After SQ1–SQ2 |
| SQ4 — Conditions | What documented goals, prompts, tools, permissions, obstacles, outside instructions, and connectivity were present? | After SQ1–SQ2 |
| SQ5 — Mechanisms | What sequence can be reconstructed: triggering context → decision/action → tool or alternative route → result? Can agent-initiated and externally directed steps be distinguished? | After SQ1–SQ2 |
| SQ6 — Reach / effects | Did behavior remain contained, get blocked, contact real external systems, or affect production data or services? Was outside access provided by the research setup rather than an actual containment escape? | After SQ1–SQ2 |
| SQ7 — Detection | How and when was behavior detected, interrupted, reported, or reconstructed? What evidence supports the timing and effects? | After SQ1–SQ2 |
| SQ8 — Synthesis | Which observed patterns recur across research, operational, and attacker-directed contexts, without confusing a selected evidence sample with general incident prevalence? | Later synthesis |

## Source-evidence category baseline (188 *sources*, not 188 confirmed incidents)

| Source-evidence category | Records |
| --- | ---: |
| Security Demonstrations & Vulnerability Reports | 91 |
| Controlled Agent Evaluations | 48 |
| Reported Operational Events | 32 |
| Attacker-Directed AI Operations | 15 |
| Unclassified — No Supported Fit | 2 |
| **Total** | **188** |

**Initial evidence-landscape observation:** 139 / 188 (73.9%) are research-demonstration, vulnerability, or controlled evaluation evidence. This reflects the collected sources, not the population rate of real-world agent failures.

## Historical next-phase plan (superseded by the agreed trajectory methodology)

The following behavior-first outline was agreed earlier on 9 November and remains here for provenance. It has been expanded into the **nine-dimension trajectory reconstruction plus separate reporting analysis** described above and in the methodology document. The current next step is a **contrasting-case pilot and discussion**, not immediate full-corpus recoding.

### Earlier plan: inductive behavior coding

1. Read the existing source-evidence records within each locked category; retain source ID, URL, original account, and evidence qualification.
2. Record the **observable action** in plain language, including whether it was attempted, blocked, or completed. Capture the agent's role; distinguish tool use, developer instruction, attacker instruction and demonstrated vulnerability.
3. Where an agent action cannot be established, record **no supported agent action**; do not invent one.
4. Let distinct recurring behavior groups emerge. Keep definitions grounded in cases and preserve counterexamples. Multiple behavior codes per source are allowed.
5. Count records exhibiting each group within each category, using **188 source records** as the current source-level corpus. Independently track deduplicated executions and case families for subsequent analysis.
6. Only then assess evidenced out-of-scope status, environments, consequences, causal hypotheses, detection and mitigation.

**Do not prematurely transform** our existing 15 inductive observations from October into an assumed final behavior taxonomy. They remain historical findings to compare against new evidence-led coding.

## Out-of-scope working definition

An action attempted or performed by an AI agent beyond its assigned task, authorized permissions, or established operating boundaries **when the evidence demonstrates that difference**. Keep **confirmed / potential / within scope / insufficient evidence** distinct. Outcome severity alone does not determine whether an action was out of scope.

## Research safeguards

- Evidence type, actor, environment of origin, reachable environment, affected system, and authorization are different fields.
- Research-origin activity can reach a live system. That does not automatically mean the agent escaped a sandbox or was unauthorized.
- An evaluation may report several runs; multiple source records may refer to the same event.
- Do not estimate real-world probabilities or causation from this selected source collection.
- Record decisions in [RESEARCH_LOG.md](RESEARCH_LOG.md) before changing definitions, numbers or source classifications.

**Current status (9 November):** Category-fit review complete; the nine-dimension methodology is documented; **new trajectory coding and comparative findings have not yet been finalized**.
