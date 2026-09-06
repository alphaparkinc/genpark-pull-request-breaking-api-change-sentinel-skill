from client import PullRequestBreakingApiChangeSentinelClient

def main():
    client = PullRequestBreakingApiChangeSentinelClient()
    res = client.audit_pr_breaking_changes()
    print('Breaking Change Sentinel: ' + res['audit_run_id'] + ' (PR #' + str(res['pr_number']) + ')')
    print('Breaking: ' + str(res['has_breaking_changes']) + ' | SemVer: ' + res['semver_recommendation'])
    print('Diff Report URL: ' + res['diff_report_url'])

if __name__ == '__main__':
    main()
