def build_json(repo, issues=None, issue_type="issue"):
    if issues is None:
        return {repo: {}}
    return {repo: [{f"{issue_type}_name": issue.title} for issue in issues]}
