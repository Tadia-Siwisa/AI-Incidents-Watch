#!/usr/bin/env python3
"""Build the evidence-aware exploratory analysis layer and figures.

The factual rebuild remains authoritative.  This script adds conservative,
case-level analytical coding for recurring dimensions that are stated in the
rebuilt findings.  Empty or unsupported details remain ``unknown``.  The
coding is multi-label, so category totals need not sum to the number of cases.
"""

from __future__ import annotations

import csv
import json
import os
from collections import Counter, defaultdict
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/ai-incidents-matplotlib")
os.environ.setdefault("XDG_CACHE_HOME", "/tmp/ai-incidents-cache")

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "rebuilt"
ANALYSIS = ROOT / "analysis"
TABLES = ANALYSIS / "tables"
FIGURES = ROOT / "reports" / "figures"


def labels(value: str) -> list[str]:
    return [] if value in {"", "unknown", "none_observed", "not_applicable"} else value.split("|")


def coding(
    organization: str,
    system: str,
    environment: str,
    actions: str,
    effects: str,
    effect_status: str,
    scope_relation: str,
    conditions: str,
    detection_timing: str,
    detector: str,
    response: str,
    date_precision: str,
) -> dict[str, str]:
    return {
        "organization_or_operator": organization,
        "system_or_model": system,
        "environment": environment,
        "action_types": actions,
        "effect_types": effects,
        "effect_status": effect_status,
        "scope_relation": scope_relation,
        "supported_contributing_conditions": conditions,
        "detection_timing": detection_timing,
        "detector": detector,
        "documented_response": response,
        "date_precision": date_precision,
    }


# These codes summarize supported findings rather than the imported workbook
# labels.  "Alleged" effects preserve the fact that a report exists without
# treating its cause or consequence as established.
CODE: dict[str, dict[str, str]] = {
    "N01": coding("Replit / SaaStr", "Replit Agent", "live_operational_use",
        "data_or_system_modification|instruction_or_scope_noncompliance|inaccurate_self_report",
        "integrity|availability", "qualified_real_effect", "crossed_operator_instruction",
        "unknown", "during_or_near_term", "user_or_operator", "earlier_version_recovered", "exact_day_range"),
    "N02": coding("Anthropic", "early Opus 4.6 agent", "internal_research_or_training",
        "external_access_or_exploitation|credential_access_or_use|data_or_system_modification",
        "confidentiality|integrity", "supported_real_effect", "left_intended_evaluation_target",
        "continued_after_task_failure|reachable_real_system|guessable_password",
        "retrospective", "lab_or_evaluator", "affected_parties_notified", "month_only"),
    "N03": coding("User / Anthropic product", "Claude Code", "live_operational_use",
        "data_or_system_modification|instruction_or_scope_noncompliance",
        "integrity|availability", "qualified_real_effect", "crossed_operator_instruction",
        "system_execution_access|wrong_host_or_target", "during_or_near_term", "user_or_operator",
        "issue_closed_without_vendor_finding", "exact_day"),
    "N04": coding("User / gym service", "unknown agent", "live_operational_use",
        "external_transaction_or_service_action|instruction_or_scope_noncompliance",
        "integrity|availability", "qualified_real_effect", "crossed_operator_instruction",
        "live_service_access", "during_or_near_term", "user_or_operator", "agent_disclosed_action_no_reversal", "month_only"),
    "N05": coding("PocketOS / Cursor / Railway", "Cursor with Claude Opus 4.6", "live_operational_use",
        "credential_access_or_use|data_or_system_modification",
        "integrity|availability", "supported_real_effect", "wrong_resource_or_target",
        "credential_mismatch|production_capable_token|destructive_endpoint_without_confirmation",
        "during_or_near_term", "user_or_operator", "provider_restored_data", "exact_day"),
    "N06": coding("Anthropic", "Opus 4.7 agents", "internal_research_or_training",
        "external_access_or_exploitation|data_or_system_modification",
        "confidentiality|integrity", "supported_real_effect", "left_intended_evaluation_target",
        "target_name_collision|internet_connected_evaluation", "retrospective", "lab_or_evaluator",
        "runs_ended_with_backend_stop|affected_party_response_not_detailed", "multi_month_range"),
    "N07": coding("Anthropic", "Mythos 5", "internal_research_or_training",
        "external_publication_or_communication|credential_access_or_use|external_access_or_exploitation",
        "confidentiality|integrity", "supported_real_effect", "left_intended_evaluation_target",
        "public_package_registry|automatic_third_party_installation|live_credentials",
        "retrospective", "lab_or_evaluator", "package_removed_and_parties_notified", "multi_month_range"),
    "N08": coding("Anthropic", "internal research model", "internal_research_or_training",
        "external_access_or_exploitation|credential_access_or_use|data_or_system_modification",
        "confidentiality|integrity", "supported_real_effect", "left_intended_evaluation_target",
        "reachable_third_party|internet_connected_evaluation|discoverable_credentials",
        "retrospective", "lab_or_evaluator", "agent_eventually_stopped|affected_party_response_not_detailed", "multi_month_range"),
    "N09": coding("Google / Irregular", "Gemini agents; versions undisclosed", "third_party_evaluation",
        "external_access_or_exploitation|credential_access_or_use",
        "confidentiality", "supported_real_effect", "left_intended_evaluation_target",
        "internet_connected_evaluation|guessable_or_public_credentials", "unknown", "lab_or_evaluator",
        "agents_stopped|affected_parties_notified", "month_only"),
    "N10": coding("OpenAI / DSEWiki", "OpenAI agents; versions undisclosed", "internal_research_or_training",
        "external_publication_or_communication|cross_agent_coordination",
        "integrity|availability", "qualified_real_effect", "left_intended_evaluation_target",
        "public_write_access|external_coordination_channel", "external_or_independent_discovery",
        "affected_external_party_or_researcher", "administrator_response_documented", "multi_month_range"),
    "N11": coding("OpenAI", "internal model", "internal_research_or_training",
        "external_publication_or_communication|credential_exposure|instruction_or_scope_noncompliance",
        "confidentiality|integrity", "supported_real_effect", "crossed_operator_instruction",
        "public_repository_write_access|secret_scanning_evasion|interventions_did_not_stop_action",
        "during_or_near_term", "user_or_operator", "keys_revoked_and_model_temporarily_removed", "exact_day"),
    "N12": coding("OpenAI / Services Australia", "internal model", "internal_research_or_training",
        "external_access_or_exploitation|credential_access_or_use",
        "confidentiality", "supported_real_effect", "left_intended_task_scope",
        "reachable_nonpublic_service|external_network_access", "retrospective", "lab_or_evaluator",
        "government_notified", "exact_day"),
    "N13": coding("OpenAI / NSW government", "model undisclosed", "internal_research_or_training",
        "external_access_or_exploitation", "confidentiality", "supported_real_effect", "left_intended_task_scope",
        "reachable_nonpublic_service|external_network_access", "retrospective", "lab_or_evaluator",
        "government_notified", "month_only"),
    "N14": coding("OpenAI / Hugging Face / Modal", "research model", "internal_research_or_training",
        "external_access_or_exploitation|credential_access_or_use|data_or_system_modification",
        "confidentiality|integrity", "supported_real_effect", "left_intended_evaluation_target",
        "internet_access|exposed_credentials|third_party_code_execution|zero_day_route",
        "retrospective", "lab_or_evaluator", "technical_investigation_and_disclosure", "exact_day_range"),
    "N15": coding("UK AISI / Anthropic / OpenAI", "Mythos 5 and GPT-5.6 Sol", "third_party_evaluation",
        "attempted_external_action", "none_observed", "attempt_only_no_observed_effect",
        "left_intended_evaluation_target", "internet_enabled|safety_classifiers_disabled",
        "during_or_near_term", "formal_monitoring", "runs_stopped_and_systems_isolated_within_about_one_hour", "exact_day_range"),
    "N16": coding("Origin", "Codex launching Claude Code", "live_operational_use",
        "control_or_approval_bypass|cross_agent_tool_use|data_access",
        "confidentiality", "qualified_real_effect", "crossed_approval_boundary",
        "nested_agent_launch|dangerous_permission_flag_available", "retrospective",
        "user_or_operator", "trace_review_reported_no_independent_vendor_finding", "report_date_only"),
    "N17": coding("OpenAI", "agent undisclosed", "internal_research_or_training",
        "external_publication_or_communication|control_or_approval_bypass",
        "external_interaction", "supported_real_effect", "left_network_boundary",
        "dns_egress_path|monitor_did_not_automatically_terminate_run", "during_or_near_term",
        "formal_monitoring", "human_acknowledged_then_run_terminated_later", "exact_day_and_time"),
    "W01": coding("OpenAI / ARC", "GPT-4", "controlled_study_or_demonstration",
        "external_publication_or_communication|deceptive_explanation",
        "human_interaction", "authorized_real_experiment", "authorized_controlled_behavior",
        "evaluator_provided_human_hiring_tool", "continuous_evaluation_observation", "lab_or_evaluator",
        "observed_within_evaluation", "year_only"),
    "W02": coding("Palisade Research", "multiple models including o3", "controlled_study_or_demonstration",
        "shutdown_or_control_interference", "none_observed", "controlled_sandbox_behavior",
        "authorized_controlled_behavior", "shutdown_test_harness", "continuous_evaluation_observation",
        "lab_or_evaluator", "observed_within_evaluation", "broad_period"),
    "W03": coding("Anthropic", "Project Vend agent", "controlled_study_or_demonstration",
        "business_or_operational_error|data_or_system_modification",
        "financial_or_operational", "authorized_real_experiment", "authorized_controlled_behavior",
        "broad_operating_authority_in_authorized_field_test", "continuous_evaluation_observation",
        "lab_or_evaluator", "observed_within_evaluation", "year_only"),
    "W05": coding("General Analysis / Cursor / Supabase", "Cursor with Supabase MCP", "controlled_study_or_demonstration",
        "prompt_injection|data_access|external_publication_or_communication",
        "confidentiality", "controlled_dummy_data_effect", "authorized_controlled_behavior",
        "untrusted_instructions|service_role_credentials|attacker_visible_output",
        "continuous_evaluation_observation", "lab_or_evaluator", "vendor_mitigations_no_customer_incident", "month_only"),
    "W06": coding("OpenAI", "agents undisclosed", "internal_research_or_training",
        "external_publication_or_communication|data_exposure",
        "confidentiality", "supported_real_effect", "left_data_handling_boundary",
        "external_upload_capability|discoverable_unlisted_urls", "unknown", "lab_or_evaluator",
        "most_images_removed_others_being_removed", "activity_date_undisclosed"),
    "W14": coding("OpenAI", "internal model", "internal_research_or_training",
        "credential_access_or_use|external_access_or_exploitation|inaccurate_self_report",
        "confidentiality", "supported_real_effect", "left_intended_task_scope",
        "public_code_search|exposed_third_party_key", "retrospective", "lab_or_evaluator",
        "incident_investigated_and_disclosed", "exact_day"),
    "W19": coding("Asymmetric Security / OpenAI-linked infrastructure", "agents undisclosed", "aggregate_external_observation",
        "external_access_or_exploitation|external_probing", "mixed_or_unknown", "mixed_qualified_activity",
        "scope_relation_varies", "mixed_or_unknown", "external_or_independent_discovery",
        "affected_external_party_or_researcher", "investigation_and_indicators_published", "multi_month_range"),
    "W21": coding("Meta / Irregular", "Muse Spark 1.1", "third_party_evaluation",
        "external_access_or_exploitation|data_or_system_modification",
        "confidentiality|integrity", "supported_real_effect", "within_mistakenly_configured_scope",
        "real_target_placed_in_prompt|internet_connected_evaluation", "unknown", "lab_or_evaluator",
        "evaluation_disabled_environment_fixed_party_notified", "month_only"),
    "W22": coding("OpenAI / Irregular", "OpenAI model undisclosed", "third_party_evaluation",
        "external_access_or_exploitation|credential_access_or_use",
        "confidentiality", "supported_real_effect", "within_mistakenly_configured_scope",
        "domain_name_collision|accidental_internet_connection", "unknown", "lab_or_evaluator",
        "evaluations_paused_issue_fixed_parties_notified", "notification_date_only"),
    "R001": coding("Reddit user / Replit", "Replit Agent", "user_reported_product_use",
        "alleged_data_or_system_modification|alleged_inaccurate_self_report",
        "integrity|availability", "alleged_unverified_effect", "alleged_or_unclear",
        "unknown", "user_reported_unknown", "user_or_operator", "unknown", "exact_post_date"),
    "R002": coding("Reddit user / Replit", "Replit Agent", "user_reported_product_use",
        "data_or_system_modification", "integrity", "product_or_configuration_effect",
        "platform_configuration_or_documented_behavior", "shared_development_and_production_database",
        "user_reported_unknown", "user_or_operator", "separate_development_database_created", "exact_post_date"),
    "R003": coding("Reddit user / Cursor", "Cursor", "user_reported_product_use",
        "attempted_data_or_system_modification", "none_observed", "attempt_only_unverified",
        "alleged_or_unclear", "user_confirmation_interface", "during_or_near_term", "user_or_operator",
        "user_skipped_action", "exact_post_date"),
    "R004": coding("Reddit user / Google", "Gemini CLI", "user_reported_product_use",
        "alleged_data_or_system_modification", "availability", "alleged_unverified_effect",
        "alleged_or_unclear", "file_move_operation", "during_or_near_term", "user_or_operator", "unknown", "exact_post_date"),
    "R005": coding("Reddit user / Google", "Gemini CLI", "user_reported_product_use",
        "alleged_data_or_system_modification", "integrity|availability", "alleged_unverified_effect",
        "alleged_or_unclear", "destructive_shell_command|path_expansion_unclear", "during_or_near_term",
        "user_or_operator", "system_restore_reported", "exact_post_date"),
    "R006": coding("Reddit user / Anthropic", "Claude Code", "user_reported_product_use",
        "data_or_system_modification|human_approval_error", "availability", "product_or_configuration_effect",
        "platform_configuration_or_documented_behavior", "explicit_approval_prompt|wrong_path_approved",
        "during_or_near_term", "user_or_operator", "unknown", "exact_post_date"),
    "R007": coding("unknown", "Claude", "user_reported_product_use",
        "alleged_data_or_system_modification", "unknown", "unsupported_no_source", "alleged_or_unclear",
        "unknown", "unknown", "unknown", "unknown", "unverified_workbook_date_only"),
    "R008": coding("Reddit user / Anthropic", "Claude CLI", "user_reported_product_use",
        "alleged_data_or_system_modification", "integrity|availability", "alleged_unverified_effect",
        "alleged_or_unclear", "destructive_shell_command|home_path_in_command", "during_or_near_term",
        "user_or_operator", "unknown", "exact_post_date"),
    "R009": coding("Reddit user / Anthropic", "Claude Code", "community_question",
        "none", "none_observed", "not_an_incident", "not_an_incident", "not_applicable",
        "not_applicable", "not_applicable", "not_applicable", "exact_post_date"),
    "R010": coding("Reddit user / Anthropic", "Claude-based repository agents", "user_reported_product_use",
        "alleged_external_publication_or_communication|alleged_instruction_noncompliance",
        "integrity", "alleged_unverified_effect", "alleged_or_unclear", "separate_agents_with_repository_access",
        "user_reported_unknown", "user_or_operator", "second_agent_reviewed_and_fixed_changes", "exact_post_date"),
    "R011": coding("Reddit user / Anthropic", "Claude Code", "user_reported_product_use",
        "alleged_instruction_noncompliance|alleged_inaccurate_self_report",
        "workflow_reliability", "alleged_unverified_effect", "alleged_or_unclear", "unknown",
        "during_or_near_term", "user_or_operator", "unknown", "exact_post_date"),
    "R012": coding("Reddit user / Replit", "Replit Agent", "user_reported_product_use",
        "alleged_data_or_system_modification", "integrity|availability", "alleged_unverified_effect",
        "alleged_or_unclear", "possible_schema_push_unconfirmed", "during_or_near_term", "user_or_operator",
        "provider_investigated_and_restored_data", "exact_post_date_to_month_range"),
    "R013": coding("Reddit user / Replit", "Replit Agent", "user_reported_product_use",
        "alleged_data_or_system_modification", "integrity|availability", "alleged_unverified_effect",
        "alleged_or_unclear", "shared_or_single_database", "during_or_near_term", "user_or_operator",
        "older_checkpoint_restored", "exact_post_date"),
    "R014": coding("Reddit user / Replit", "Replit Agent", "user_reported_product_use",
        "alleged_data_or_system_modification", "none_observed", "core_effect_contradicted",
        "contradicted_claim", "unknown", "during_or_near_term", "user_or_operator",
        "vendor_representative_reported_database_and_data_present", "exact_post_date"),
    "R015": coding("Reddit user / Anthropic", "Claude Code", "product_documentation_or_configuration",
        "documented_data_retention_cleanup", "availability", "product_or_configuration_effect",
        "platform_configuration_or_documented_behavior", "default_30_day_cleanup_setting",
        "user_reported_unknown", "user_or_operator", "configurable_retention_documented", "exact_post_date"),
    "R016": coding("Reddit user / Replit", "Replit platform", "user_reported_product_use",
        "platform_configuration_change", "none_observed", "agent_causation_contradicted",
        "contradicted_claim", "platform_inserted_unintended_secret", "during_or_near_term", "user_or_operator",
        "vendor_identified_platform_incident", "exact_day_range"),
    "R017": coding("Reddit user / Anthropic", "Claude Code", "user_reported_product_use",
        "alleged_data_or_system_modification|alleged_safeguard_removal",
        "integrity|availability", "alleged_unverified_effect", "alleged_or_unclear",
        "mutation_test_removed_guard|real_delete_function_available", "during_or_near_term", "user_or_operator",
        "unknown", "exact_post_date"),
    "R018": coding("Reddit user / Anthropic", "Claude Code", "user_reported_product_use",
        "alleged_data_or_system_modification", "integrity|availability", "alleged_unverified_effect",
        "alleged_or_unclear", "background_command|destructive_command_unrecoverable", "during_or_near_term",
        "user_or_operator", "unknown", "exact_post_date"),
    "R019": coding("Reddit user / Anthropic", "Claude Code", "user_reported_product_use",
        "alleged_data_or_system_modification|alleged_instruction_noncompliance",
        "integrity|workflow_reliability", "alleged_unverified_effect", "alleged_or_unclear", "unknown",
        "user_reported_unknown", "user_or_operator", "user_detected_false_positives", "exact_post_date"),
    "R020": coding("Reddit poster / Anthropic", "claimed Claude Opus 5.5", "user_reported_product_use",
        "alleged_data_or_system_modification", "unknown", "unsupported_title_only", "alleged_or_unclear",
        "unknown", "unknown", "unknown", "unknown", "exact_post_date"),
}


MODEL_DEVELOPER: dict[str, str] = {
    **{key: "OpenAI" for key in ["N10", "N11", "N12", "N13", "N14", "N17", "W01", "W06", "W14", "W22"]},
    **{key: "Anthropic" for key in ["N02", "N03", "N05", "N06", "N07", "N08", "W03", "R006", "R007", "R008", "R009", "R010", "R011", "R015", "R017", "R018", "R019", "R020"]},
    **{key: "Replit" for key in ["N01", "R001", "R002", "R012", "R013", "R014"]},
    **{key: "Google" for key in ["N09", "R004", "R005"]},
    "N04": "unknown",
    "N15": "multiple_or_cross_provider",
    "N16": "multiple_or_cross_provider",
    "W02": "multiple_or_cross_provider",
    "W05": "unknown",
    "W19": "OpenAI_linked_not_confirmed",
    "W21": "Meta",
    "R003": "unknown",
    "R016": "not_applicable_platform_event",
}


def write_csv(path: Path, rows: list[dict], fields: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fields is None:
        fields = list(rows[0]) if rows else []
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def count_rows(counter: Counter, denominator: int) -> list[dict]:
    return [
        {"category": key, "cases": value, "denominator": denominator, "percent": round(100 * value / denominator, 1)}
        for key, value in sorted(counter.items(), key=lambda item: (-item[1], item[0]))
    ]


def explode_count(rows: list[dict], field: str) -> Counter:
    result: Counter = Counter()
    for row in rows:
        for value in labels(row[field]):
            result[value] += 1
    return result


def save_bar(counter: Counter, title: str, xlabel: str, path: Path, color: str = "#37658a") -> None:
    items = sorted(counter.items(), key=lambda item: (item[1], item[0]))
    fig, ax = plt.subplots(figsize=(9.2, max(3.4, 0.48 * len(items) + 1.2)))
    names = [key.replace("_", " ") for key, _ in items]
    values = [value for _, value in items]
    bars = ax.barh(names, values, color=color)
    ax.bar_label(bars, padding=4, fontsize=9)
    ax.set_title(title, loc="left", fontsize=13, weight="bold")
    ax.set_xlabel(xlabel)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="x", alpha=0.2)
    ax.set_axisbelow(True)
    fig.tight_layout()
    fig.savefig(path, dpi=180, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    factual = json.loads((DATA / "factual_rebuild.json").read_text())
    cases = factual["cases"]
    case_ids = {case["canonical_id"] for case in cases}
    if case_ids != set(CODE) or case_ids != set(MODEL_DEVELOPER):
        raise SystemExit(
            "Coding coverage mismatch: "
            f"case_code_missing={sorted(case_ids-set(CODE))} case_code_extra={sorted(set(CODE)-case_ids)} "
            f"developer_missing={sorted(case_ids-set(MODEL_DEVELOPER))} developer_extra={sorted(set(MODEL_DEVELOPER)-case_ids)}"
        )

    rows = []
    for case in cases:
        cid = case["canonical_id"]
        if case["eligible_for_confirmed_incident_analysis"]:
            analytical_scope = "higher_confidence_confirmed"
        elif case["eligible_for_qualified_or_wider_analysis"]:
            analytical_scope = "wider_supported_only"
        else:
            analytical_scope = "excluded_from_incident_pattern_analysis"
        rows.append({
            "canonical_id": cid,
            "title": case["title"],
            "claim_status": case["claim_status"],
            "disposition": case["disposition"],
            "analytical_scope": analytical_scope,
            "verified_period": case["verified_period"],
            "model_developer_family": MODEL_DEVELOPER[cid],
            **CODE[cid],
            "source_refs": "|".join(case["source_refs"]),
        })

    ANALYSIS.mkdir(exist_ok=True)
    TABLES.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    write_csv(ANALYSIS / "case_coding.csv", rows)
    (ANALYSIS / "case_coding.json").write_text(json.dumps(rows, indent=2) + "\n")

    confirmed = [row for row in rows if row["analytical_scope"] == "higher_confidence_confirmed"]
    wider = [row for row in rows if row["analytical_scope"] != "excluded_from_incident_pattern_analysis"]
    excluded = [row for row in rows if row["analytical_scope"] == "excluded_from_incident_pattern_analysis"]

    table_specs = {
        "claim_status_full.csv": (Counter(row["claim_status"] for row in rows), len(rows)),
        "disposition_full.csv": (Counter(row["disposition"] for row in rows), len(rows)),
        "analytical_scope.csv": (Counter(row["analytical_scope"] for row in rows), len(rows)),
        "environment_confirmed.csv": (Counter(row["environment"] for row in confirmed), len(confirmed)),
        "environment_wider.csv": (Counter(row["environment"] for row in wider), len(wider)),
        "model_developer_confirmed.csv": (Counter(row["model_developer_family"] for row in confirmed), len(confirmed)),
        "action_types_confirmed.csv": (explode_count(confirmed, "action_types"), len(confirmed)),
        "effect_types_confirmed.csv": (explode_count(confirmed, "effect_types"), len(confirmed)),
        "detection_timing_confirmed.csv": (Counter(row["detection_timing"] for row in confirmed), len(confirmed)),
        "effect_status_full.csv": (Counter(row["effect_status"] for row in rows), len(rows)),
    }
    for filename, (counter, denominator) in table_specs.items():
        write_csv(TABLES / filename, count_rows(counter, denominator))

    # Cross-tab environment by analytical scope.
    environments = sorted({row["environment"] for row in rows})
    scopes = ["higher_confidence_confirmed", "wider_supported_only", "excluded_from_incident_pattern_analysis"]
    cross = []
    for environment in environments:
        record = {"environment": environment}
        for scope in scopes:
            record[scope] = sum(row["environment"] == environment and row["analytical_scope"] == scope for row in rows)
        cross.append(record)
    write_csv(TABLES / "environment_by_scope.csv", cross, ["environment", *scopes])

    # Source and date audit tables.
    source_count = Counter()
    for row in rows:
        n = len([x for x in row["source_refs"].split("|") if x])
        source_count["no_traceable_source" if n == 0 else "one_source" if n == 1 else "multiple_sources"] += 1
    write_csv(TABLES / "source_coverage_full.csv", count_rows(source_count, len(rows)))
    write_csv(TABLES / "date_precision_full.csv", count_rows(Counter(row["date_precision"] for row in rows), len(rows)))

    # Named-case lists make every aggregate result auditable.
    list_rows = []
    for scope_name, subset in [("full", rows), ("wider", wider), ("confirmed", confirmed), ("excluded", excluded)]:
        for row in subset:
            list_rows.append({"scope": scope_name, "canonical_id": row["canonical_id"], "title": row["title"]})
    write_csv(TABLES / "scope_membership.csv", list_rows)

    save_bar(Counter(row["disposition"] for row in rows),
             "Evidence disposition across all 46 case families", "Case families", FIGURES / "evidence_disposition.png")
    save_bar(Counter(row["environment"] for row in confirmed),
             "Environment of the 15 higher-confidence cases", "Case families", FIGURES / "confirmed_environment.png", "#5b7f49")
    save_bar(explode_count(confirmed, "effect_types"),
             "Supported effects in the 15 higher-confidence cases", "Case families (multi-label)", FIGURES / "confirmed_effects.png", "#9a5c43")
    save_bar(Counter(row["detection_timing"] for row in confirmed),
             "Detection timing in the 15 higher-confidence cases", "Case families", FIGURES / "confirmed_detection.png", "#76558f")

    # Machine-readable headline values used by the report and validation.
    summary = {
        "input_rows": factual["metadata"]["input_record_count"],
        "canonical_case_families": len(rows),
        "duplicate_overlap_rows_removed_by_reconciliation": factual["metadata"]["input_record_count"] - len(rows),
        "higher_confidence_confirmed_cases": len(confirmed),
        "wider_supported_cases_including_confirmed": len(wider),
        "excluded_from_incident_pattern_analysis": len(excluded),
        "confirmed_environment_counts": dict(Counter(row["environment"] for row in confirmed)),
        "confirmed_effect_counts_multilabel": dict(explode_count(confirmed, "effect_types")),
        "confirmed_detection_counts": dict(Counter(row["detection_timing"] for row in confirmed)),
        "cases_with_no_traceable_source": source_count["no_traceable_source"],
    }
    (ANALYSIS / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
