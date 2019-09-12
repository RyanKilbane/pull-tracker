def build_json(operation, issues=None, repos=None):
    output_json = {operation: {}}
    if issues is None:
        return output_json
    for repo in repos:
        output_json[operation][repo] = []
    return output_json