# Evidence review method and remaining gaps

## Review state

The first source-review pass is complete for all 46 canonical families derived from 63 workbook rows. The factual outputs are:

- `data/rebuilt/factual_rebuild.json`
- `data/rebuilt/factual_rebuild.csv`
- `data/rebuilt/factual_claims.json` and `.csv`
- `data/rebuilt/factual_sources.json`
- `evidence/cases/*.md`

The original workbooks, imported rows, and field assertions remain available as a separate assertion layer. A workbook label such as “confirmed,” “high confidence,” or “company response” did not carry into the factual layer unless retrieved evidence supported it.

## Evidence standard

The review applied these rules:

1. A source must contain a relevant passage. A homepage, report index, generic documentation page, or search result is not evidence for a case.
2. Primary lab/operator disclosures establish what the disclosing organization reports. Independent or affected-party evidence is recorded separately where available.
3. A direct user post establishes that an allegation was made. It does not by itself prove product causation, the command executed, or the scale of damage.
4. Screenshots and logs are direct artifacts with provenance limits. A proposed command is not recorded as executed unless the evidence shows execution.
5. Task, permission boundary, action, target, effect, mechanism, attribution, detection, and disclosure timing are treated as separate factual questions.
6. Conflicting evidence is preserved. A later vendor explanation or author correction changes the adjudication rather than being hidden in notes.
7. Counts inside a family are not promoted into independent incident counts without identifiable, independently supportable event units.
8. Recorded model reasoning is evidence of text produced during a run. It is not treated as direct proof of a model's internal belief or intent.

## Disposition fields

- `include_confirmed`: a real external action or effect is supported by a primary disclosure or strong corroboration.
- `include_with_qualification`: a material case is supported, but attribution, scope, or independence is limited.
- `retain_as_controlled_context`: the behavior occurred in an authorized study or evaluation and belongs in the wider comparison set.
- `retain_as_product_context`: documentation, configuration, or human approval explains the observation better than autonomous boundary crossing.
- `hold_unverified`: a direct allegation remains useful as a lead but lacks enough corroboration for incident analysis.
- `reject_core_claim`: retrieved evidence contradicts the central incident or agent-causation claim.
- `reject_as_non_incident`: the record contains no observed incident.

`eligible_for_confirmed_incident_analysis` is intentionally strict. `eligible_for_qualified_or_wider_analysis` adds qualified and controlled cases but still excludes unverified Reddit leads, product context, contradictions, and non-incidents.

## Source route and preservation

The environment exposed no authorized browser or search connector. Its enforced permission profile allowed unrestricted outbound network access, which provided an authorized alternative. The review used direct HTTPS retrieval and DuckDuckGo's HTML search route, then opened the relevant source pages rather than relying on search snippets.

All 32 supplied URLs were retrieved. Additional sources were located for the ten canonical families that lacked a supplied citation and for cases whose supplied citation did not support the incident detail. HTML/PDF bodies and text conversions are stored locally. `factual_sources.json` binds every cited source to its URL, evidence tier, locator, local file, retrieval date, byte count, and SHA-256 hash.

Reddit's main pages returned anti-bot responses. Public Reddit embed pages supplied post bodies and timestamps. PullPush comments are retained as third-party archive copies and never described as direct Reddit retrieval. The comments were especially relevant to R006, R012-R014, and R016.

## Major factual decisions

- **R003:** attempted deletion supported by screenshot; the user skipped it, so no completed deletion is recorded.
- **R006:** the author admits approving the wrong path. Retained as human-approval/product-control context.
- **R009:** a security question, not an incident.
- **R012:** reported loss, failed restores, vendor investigation, and eventual recovery are supported; agent causation remains unresolved.
- **R013:** reported loss and partial checkpoint recovery are supported; a shared/single database configuration confounds agent causation.
- **R014:** rejected because Replit said the Neon database and data still existed.
- **R015:** the 30-day silent cleanup default is documented product behavior; universal/permanent unrecoverability is not established.
- **R016:** rejected as agent-caused. Replit attributed the behavior to its August 31/September 1 platform incident.
- **R017:** the screenshot series is unusually detailed, but remains a user-supplied artifact without independent machine telemetry.
- **R020:** title only; no original account, body, evidence link, or useful archived comments.
- **N01, N03, N04, N16:** retained with qualifications because evidence is an attributed operational account, user issue, interview, or operator trace without full independent confirmation.
- **N02, N05-N09, N11-N14, N17, W06, W14, W21, W22:** core real-system action is sufficiently supported for the confirmed set.
- **N10:** external wiki coordination is supported at OpenAI category level; DSEWiki-specific totals come from independent reconstruction.
- **N15:** supported, but moved to wider scope because attempts failed and AISI reported no real-world harm.
- **W01-W03 and W05:** controlled or authorized context, retained for wider analysis.
- **W19:** useful independent forensic reconstruction, but unsuitable for converting every observed service/domain into a separate incident.

## Remaining evidence gaps

- R007 has no URL or identifiable source.
- R001, R003-R005, R008, R010-R011, R017-R019 remain direct-user allegations or artifacts without independent product telemetry.
- R020 lacks the underlying account entirely.
- N03 has no Anthropic finding; its GitHub issue was closed automatically after inactivity.
- N04 lacks a published gym/API audit and the exact model identity remains uncertain.
- N09's company identities and model versions are undisclosed. The “sworn confirmation Oct 5” detail was not found.
- N10's detailed run/edit counts are independently reconstructed, not case-level OpenAI telemetry.
- N16 has not been independently confirmed by OpenAI or Anthropic.
- W06's per-image dates, motives, and run identities are not disclosed.
- W19 contains mixed-confidence attribution and should remain an aggregate investigation.

These gaps are encoded in each case's `corrections_or_unresolved` field. Future evidence can be added without changing the preserved import layer.
