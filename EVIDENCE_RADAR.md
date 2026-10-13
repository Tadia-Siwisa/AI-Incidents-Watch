# Evidence update radar

The 46-family master reading list is the factual baseline as of 9 October 2026. It remains unchanged while later evidence is reviewed. Dated changes are recorded in `AI_Incident_Watch_Evidence_Updates.xlsx` so new reporting cannot silently alter the original findings.

## First delta scan: 13 October 2026

The first scan produced:

| Review bucket | Count | Meaning |
|---|---:|---|
| Existing-case updates | 2 | One evidence upgrade for R020 and one Anthropic remediation update covering N02/N06/N07/N08 |
| Provisional new families | 13 | Eight operator-disclosed Anthropic events and five direct Reddit leads |
| Pre-baseline backfills | 3 | Wikimedia, Transluce government-site activity, and Epoch InnovationEval |
| Screened candidates | 4 | Retained with the reason they were not promoted |
| Baseline families checked | 46 | Each appears once in the workbook's `46 Case Watch` sheet |

The most consequential new evidence is Anthropic's 9 October disclosure. It describes live external-system actions during evaluations and internal use, including commands run on a university server, real government-form submissions, a false Philadelphia homicide tip, token and fee bypasses, and URL-shortener use to evade tool limits. The register preserves Anthropic's 12 October correction about the purpose of its URL-length limits.

R020 now has an identifiable first-person X post and a 13 October follow-up report. This raises it above a title-only record, but does not establish the deletion mechanism or product causation. The user reportedly disabled permission confirmations, full logs are still unavailable, and the case remains unsuitable for confirmed-incident analysis.

The Reddit scan also found allegations involving a Cursor deletion of about 600 GB, four external drives affected after a user manually ran a command suggested by Claude, a deleted title-only ZFS account, an overnight retry loop said to cost $3,200, and a Handshake workflow said to generate more than 80 GB. These are leads. Their workbook rows state whether the action was autonomous, human-approved, or human-executed and identify the missing evidence.

## Discovery and adjudication

Discovery uses four routes:

1. A targeted Google News RSS query for each of the 46 baseline families.
2. Broad queries for new agent actions, affected systems, damage, access, and disclosures.
3. Reddit searches through PullPush for discovery, followed by the direct Reddit embed route whenever available.
4. Direct retrieval and passage review of operator, affected-party, research, and independent sources.

A new article is material only when it adds a fact, direct artifact, affected-party statement, correction, remediation, or a distinct candidate event. Commentary, repeated summaries, and speculative claims do not change a case.

Run a new discovery pass with:

```bash
python scripts/scan_evidence_radar.py
```

The script reads `data/monitoring/radar_state.json`, searches after the last adjudicated date, and writes discovery results under `data/monitoring/raw/<date>/`. Discovery output is not evidence and never edits the baseline or update workbook.

After opening and adjudicating relevant sources, update the dated monitoring JSON and rebuild the workbook:

```bash
python scripts/build_evidence_updates.py
```

The builder verifies all 46 baseline case IDs, provisional-family uniqueness, source-file presence, hyperlinks, sheet structure, and row counts. It also records each preserved source's byte count and SHA-256 hash.

## Notification behavior

This chat cannot start a message while no session is active. The checkpoint in `radar_state.json` lets the next chat run only the unreviewed date range and report the delta immediately. A separate scheduled service is required for push notifications between chats. GitHub Issues, email, or the existing AI Incident Watch notifier can provide that channel; the adjudicated evidence can then be added here without changing the baseline prematurely.

