def filter_issues(issues):
    repos_with_issues = {}
    for repo in issues:
        if not issues[repo]:
            continue
        repos_with_issues[repo] = issues[repo]
    print(repos_with_issues)
    return repos_with_issues