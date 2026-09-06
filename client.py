class PullRequestBreakingApiChangeSentinelClient:
    def audit_pr_breaking_changes(self, pr_number=142, base_branch='main', head_branch='feature/v2-refactor', target_schema='openapi.json'):
        return {
            'audit_run_id': 'brk_chg_8812',
            'pr_number': pr_number,
            'target_schema': target_schema,
            'has_breaking_changes': False,
            'deleted_routes_count': 0,
            'narrowed_types_count': 0,
            'optional_parameters_added': 2,
            'semver_recommendation': 'MINOR_BACKWARD_COMPATIBLE',
            'diff_report_url': 'https://audit.codereview.genpark.ai/prs/142/breaking-changes.json'
        }
