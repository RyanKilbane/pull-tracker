from utils.get_reviewers import get_reviewers
from utils.get_user_details import get_user_details
def build_json(repo, issues=None, issue_type="issue"):
    if issues is None:
        return {repo: {}}
    return {repo: [{f"{issue_type}_name": issue.title, 
                    f"{issue_type}_number": issue.number, 
                    "reviewers": get_user_details(get_reviewers(issue.number, "ONSDigital", repo))} for issue in issues]}
