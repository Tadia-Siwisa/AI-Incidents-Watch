# AI Agent Incident Watch

**Independent, evidence-led research into AI-agent actions, authorization boundaries, and the environments in which agents operate.**

**Research update: 22 October 2026 · Status: exploratory analysis and ongoing evidence review**

AI agents act through tools, credentials, APIs, files, and networks. When unexpected actions occur, the immediate explanation is not always “the model disobeyed.” The cause could involve the assigned task, configured targets, permissions, infrastructure, a vulnerable application, human approval, or the agent's actions—and sometimes the reported event is not supported by the available evidence.

**Our purpose is to document what is currently observable and possible, distinguish claims from established facts, and learn how agent behavior interacts with the systems around it.** We are not starting with a predetermined failure mechanism or defensive product.

The recurring questions are: **What was the objective? What tools, permissions, credentials, and access did the agent actually have? What did it do? What boundary or expectation was involved? What happened next? How was it detected, and what can the evidence establish?**

## Research progress at a glance

The study has expanded through several distinct stages. **These numbers are not interchangeable, additive, or counts of unique confirmed incidents.**

| Research stage | Scope | Meaning and location |
| --- | ---: | --- |
| Initial factual reconciliation — 9 Oct | **46 case families** from 63 imported rows | Original adjudicated baseline. Of these, 15 met its strict threshold and 26 qualified for wider evidence-supported analysis. **In this repository.** |
| Wide Search 2 — 14 Oct | **225 source/candidate records** | 171 Permission Protocol, 44 METR, and 10 directly researched records; includes overlaps, controlled evaluations, security demonstrations, reported events, and screened cases. **In this repository.** |
| Later evidence-gate review — 21 Oct | **188 selected records** | Subsequent reviewed working collection drawn from the broad candidate set. Some source claims remain only partly verified; the entries are not necessarily independent events. **Current research workbook is outside this repository.** |
| Preliminary inductive analysis — 21 Oct | **15 overlapping observations** | Initial open-ended reading and grouping of the 188 records, with case-to-pattern links. These are provisional themes rather than final causal categories. **Working workbook is outside this repository.** |
| Continuous intake — from 22 Oct | **Live candidate queue** | GitHub Issue submissions synchronized to a separate unverified JSON/Excel intake register. **Operational in this repository.** |

The **188-record** analytical pool contains different kinds of material: **38 controlled agent evaluations, 35 reported operational events, 93 controlled security demonstrations or vulnerability records, 16 attacker-directed AI-use records, and 6 reporting-reliability records.** The evidence gate distinguished **40 verified and 148 partly verified source records** under its working criteria. This is *not* confirmation of 188 autonomous-agent boundary-crossing incidents: evidence strength, agent causation, authorization, and real-world impact must be considered separately.

The 46-family baseline and 225-record discovery register remain preserved. Their original reports and scripts are **historical research artifacts**, not replacements for the newer evidence-gated working collection.

## How the research is conducted

### 1. Gather and preserve candidate records

We bring together direct incident reports, operator and laboratory disclosures, independent reporting, public research registers, user accounts, controlled evaluations, and vulnerability demonstrations. Sources and original claims are retained with their provenance.

### 2. Verify claims and distinguish event types

We check whether a source substantiates the specific claim, seek independent or affected-party accounts where possible, and preserve corrections and uncertainty. We distinguish:

- reported operational incidents from controlled tests or authorized adversarial games;
- demonstrated software vulnerabilities from confirmed in-the-wild exploitation;
- actions attempted, blocked, executed, or only alleged;
- an agent's technical access from the authorization of its user or an affected institution;
- source-level support from proof of model causation or internal intent.

A reachable URL or a headline is not proof of the underlying event. A credential granting access does not mean every possible action was authorized. A model's written explanation is not direct access to its internal representations.

### 3. Reconstruct what happened

Our case-level reading focuses on:

`objective → environment / tools / permissions → actions → boundary interaction → observed result → detection and response`

We record what is known and mark unknown or disputed stages rather than filling gaps. Detection, alerting, acknowledgement, intervention, notification, and retrospective discovery are separate events.

### 4. Explore natural groupings before finalizing a taxonomy

The first inductive reading produced **15 provisional, non-exclusive observations**. Illustrative recurring material includes:

- product or infrastructure vulnerabilities that expose agent workflows, sometimes **without** evidence of model misbehavior;
- resource or execution boundary crossing;
- instructions embedded in untrusted content reaching higher-trust workflows;
- access via credentials, tokens, or identities;
- alteration of task-success evidence, scores, tests, or outputs;
- different tactics after an obstruction;
- actions with effects beyond the requested or authorized scope.

These are **qualitative, data-led themes** rather than a validated statistical clustering result or a settled taxonomy. A record can exhibit several patterns. The next analytical step is to examine *each provisional category in depth*, asking how events unfolded, what differed between cases, and which apparent patterns survive closer evidence review.

**Research caution:** The 188-record inductive analysis was performed from previously assembled source descriptions and evidence-review notes, rather than complete primary execution logs for every case. Source-selection bias, repeated underlying case families, and study-specific concentrations prevent generalizing its raw counts to real-world incident frequency.

## What is actually in this repository?

| Resource | What it contains |
| --- | --- |
| [Initial factual register](data/rebuilt/factual_rebuild.json) | Evidence-adjudicated findings for the 46 original case families |
| [Master reading list](AI_Incident_Watch_Master_Reading_List.xlsx) | Historical baseline reading workbook |
| [Combined 46 + Wide Search 2 workbook](AI_Incident_Watch_Combined_46_and_Wide_Search_2.xlsx) | An earlier combination of the baseline and expanded discovery set, **not** the latest evidence-gated master |
| [Wide Search 2 workbook](AI_Incident_Watch_WIDE_Search_2.xlsx) | The 225 candidate/source records |
| [Wide Search 2 documentation](WIDE_SEARCH_2.md) | Definitions, methods, original source routes, duplication and evidence cautions |
| [Evidence updates workbook](AI_Incident_Watch_Evidence_Updates.xlsx) | Dated updates and leads from the original monitoring pass |
| [Exploratory 46-family report](reports/AI_Agent_Incident_Exploratory_Analysis.md) | Historical analysis of the original population, not the later 188-record study |
| [Verification approach](VERIFICATION.md) | Original evidence standard, dispositions, and corrections |
| [Evidence Radar](EVIDENCE_RADAR.md) | Historical research monitoring methodology |
| [Live incident intake workbook](data/intake/incident_leads.xlsx) | Unverified incoming leads from GitHub Issues |
| [Incident intake guide](docs/INCIDENT_INTAKE.md) | Instructions and current automation limitations |

Original imported spreadsheets are preserved under `data/original/`; the 46-family factual review under `data/rebuilt/` and `evidence/cases/`; Wide Search 2 machine-readable material under `data/wide_search_2/`; scripts under `scripts/`; historical analyses and reports under `analysis/` and `reports/`.

**Version distinction:** The October 21 evidence-gate and inductive-analysis workbooks have **not yet been committed to this repository**. Until they are synchronized and versioned, no file in this repository should be presented as the latest 188-record master or as a published final taxonomy.

## New incidents: intake and review

Our current workflow is:

1. **Discover:** a report or disclosure appears in an AI Frontier Watch briefing, another conversation, or a research source.
2. **Check:** review the source, the precise claims, conflicting information, possible duplicates, what kind of case it is, and what remains unverified.
3. **Submit:** create a source-linked [GitHub incident lead Issue](https://github.com/Tadia-Siwisa/AI-Incidents-Watch/issues/new/choose), or explicitly ask a connected assistant to submit it.
4. **Sync:** [GitHub Actions](.github/workflows/incident-intake.yml) updates `data/intake/incident_leads.json` and [the intake workbook](data/intake/incident_leads.xlsx), keyed by GitHub Issue number.
5. **Review and promote deliberately:** adjudicate case-level evidence and duplication before adding the lead to any curated research population. The original datasets and preliminary taxonomy do not change automatically.

**Automated now:** GitHub Issue → unverified JSON/Excel intake workbook. **Not automated:** searching all conversations, independent source verification, adjudicating claims, consolidating duplicates across publications, updating the research master, or recomputing a taxonomy.

The [synthetic pipeline test (Issue #2)](https://github.com/Tadia-Siwisa/AI-Incidents-Watch/issues/2) is **not a real incident**. The [US bank access reporting lead (Issue #3)](https://github.com/Tadia-Siwisa/AI-Incidents-Watch/issues/3) is explicitly **unverified**, with no independently established rogue agent transaction or specific autonomous boundary crossing.

## Rebuilding historical artifacts

From the repository root, with the Python dependencies required by the scripts installed:

```bash
python scripts/rebuild_register.py
python scripts/build_factual_rebuild.py
python scripts/analyze_incidents.py
python scripts/build_wide_search_2.py
python scripts/build_evidence_updates.py
```

These commands rebuild the **existing dated research layers** from their corresponding inputs. They do not import the latest off-repository evidence-gated workbook or automatically include intake Issues in the research dataset. For discovery-only scans, see [Evidence Radar](EVIDENCE_RADAR.md) and `scripts/scan_evidence_radar.py`.

## Immediate research priorities

1. **Bring the current evidence-gated workbooks and inductive case links into the repository**, preserving dated baselines and change provenance.
2. **Study each emerging category individually**: its objectives, vulnerabilities or access paths, actions, obstructions, outcomes, counterexamples, and evidence quality.
3. **Make review decisions traceable**, so newly disclosed incidents can enter the intake queue, be verified, and eventually update a curated master without silently changing earlier findings.

We are keeping the space of possible explanations open while making the evidence, research stages, and next actions explicit.
