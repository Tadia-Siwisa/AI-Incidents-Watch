# Automated evidence intake and reviewed-dataset promotion

**Owner:** AI Agent Incident Watch  
**Status:** Two-stage workflow. Automated intake is *unverified*; promotion requires explicit researcher approval.

## Pipeline at a glance

1. Daily AI Frontier Watch and AI Agent Incident Watch tasks discover new source disclosures and substantive updates to known cases.
2. The task checks the repository's existing intake issues and, if connected GitHub write access is available, creates one **owner-authored** \`[Evidence]\` GitHub issue for each distinct primary source/disclosure date. It includes a source URL, any existing case match, and uncertainty.
3. A GitHub Actions workflow \`.github/workflows/evidence-intake.yml\` converts the issue into \`data/intake/incoming_evidence.json\` and the separate **\`data/intake/incoming_evidence.xlsx\`** register. This is Stage 1.
4. The researcher reviews incoming rows in the research chat, verifies claims and case matching, and explicitly decides whether to accept, qualify, reject, or hold each item.
5. **Only with that explicit approval** is the relevant working dataset edited and its new version committed. Document decisions and source IDs in the research log. This is Stage 2.

No workflow has automatic write permission to \`data/working/\`. A reported action is not proof of an autonomous out-of-scope action.

## Stage 1 — Source intake

- Canonical register: [incoming_evidence.json](../../data/intake/incoming_evidence.json).
- Excel view: [incoming_evidence.xlsx](../../data/intake/incoming_evidence.xlsx), generated after intake.
- Source link: \`[Evidence]\` GitHub issue; author must match the repository owner.
- Fields include source URL and disclosure date, reported action, newly reported evidence, contextual category, existing case match, caveats, discovery channel, issue link, and duplicate flag.
- New record ID is \`EV-{GitHub issue number}\`.
- Repeated edits to the same issue update the same record, not an additional row.
- Same normalized source URL + disclosure date + case match across different issues is **flagged**, not silently merged or double-counted. Different disclosures about an existing case remain separate evidence updates.
- Entries are *not* assigned a confirmed incident status by collection automation.
- Owners may use the GitHub issue form to stage a source manually. Scheduled tasks should create identically structured issues via connected GitHub tools, checking existing issues before creating another.

**Known limitation:** Scheduled ChatGPT tasks must actually have GitHub connected and authorized to create an issue at run time. A daily report alone does not prove that it was staged. When writing fails, the task must clearly report "NOT STAGED — needs manual intake" with the source URL.

## Stage 2 — Human approval

The incoming register is a queue. The researcher reviews the source and related records in chat before any dataset edits.

| Decision | Effect |
| --- | --- |
| **Accept — new record** | Create a genuinely new case only after verifying no matching existing case or source family. |
| **Accept — update existing** | Add an evidence update to the identified existing case; preserve earlier status/date and provenance. |
| **Qualified / hold** | Keep pending with uncertainty; do not promote into confirmed incidents. |
| **Reject / duplicate** | Retain a documented disposition in review notes, without adding a new incident. |

Changes to the 188-source workbook or subsequent reviewed data snapshots require the researcher's explicit approval and a logged explanation. **Automation never silently changes classifications or case counts.**

## Backfill and missing-disclosure checks

- At first operational run, compare dated sources from 1 November 2026 onward to existing cases, GitHub intake entries, and previous reports. Stage only substantive additions, updates or corrections not already queued.
- Thereafter search an overlapping recent window (e.g. last 7 days) rather than relying exclusively on today's publications. Older incidents may have new disclosures.
- Distinguish **incident date**, **disclosure date**, **date found**, and **last substantive update**.
- \`data/monitoring/radar_state.json\` is a *historical October checkpoint*, not the source of truth for the current reviewed 188-source corpus.
- The monitoring automation's last run is not equivalent to an evidence adjudication.

## Safeguards and troubleshooting

- The GitHub Action only commits \`data/intake/incoming_evidence.json\` and \`data/intake/incoming_evidence.xlsx\`.
- The independent prior \`[Incident]\` lead-intake workflow is unchanged.
- The \`incoming_evidence.json\` is authoritative for the incoming workbook; never edit the generated workbook directly.
- Spreadsheet formula injection is escaped, and potentially matching URLs are normalized without erasing original source links.
- A failed Actions run means the report may exist as an issue but **not yet in the workbook**. Check [GitHub Actions](https://github.com/Tadia-Siwisa/AI-Incidents-Watch/actions/workflows/evidence-intake.yml).
- Search for \`[Evidence]\` issues before filing repeated items or doing a backfill.
