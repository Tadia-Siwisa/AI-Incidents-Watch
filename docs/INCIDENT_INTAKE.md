# Incident intake pilot

A new GitHub issue filed using **New AI agent incident lead** becomes a pending, unverified lead. The workflow does not edit existing research evidence, verified datasets, or the 188-case inductive taxonomy.

## From any ChatGPT conversation
Explicitly ask to submit the documented incident to this repository as a GitHub issue and provide its source. Discussing it in a chat alone does **not** synchronize anything.

## Workflow
1. Repository owner creates a new issue from the form. The public repository means never include confidential logs, secrets, passwords, or personal data.
2. GitHub Action runs on new/edited/reopened owner-created [Incident] issues.
3. It upserts a row into `data/intake/incident_leads.json` and rebuilds `data/intake/incident_leads.xlsx`.
4. Researchers manually deduplicate, verify, correct, and promote records to the evidence-backed main dataset.

This intake workbook is *separate* from the October 21 evidence-gated corpus and from the pre-existing baseline. A GitHub issue is a lead, not an established incident.

## Setup
Merge the pull request. Confirm GitHub Actions is enabled and the repository workflow token permits write access to contents. Create a test issue from the form and confirm an entry is added by the workflow.

## Limitations
The workflow does not poll the web, ingest arbitrary messages, or verify evidence. It does not handle source-level deduplication automatically. Issue edits replace the row by issue number. The `workflow_dispatch` command rebuilds the sheet from current saved rows.
