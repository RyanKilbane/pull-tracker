def build_json(repo, issues=None):
    if issues is None:
        return {repo: {}}
    return {repo: [{"issue_name": issue.title} for issue in issues]}
