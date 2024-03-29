from backend.utils.get_reviewers import get_reviewers
from backend.utils.get_user_details import get_user_details
from backend.construct_setup_yaml import setup_data
import yaml

def build_json_threads(repo, issue_type="pull"):
    issues = repo.get_pulls(state="open")
    return {repo.name: [{f"{issue_type}_name": issue.title, 
                       f"{issue_type}_number": issue.number, 
                       "reviewers": get_user_details(get_reviewers(issue.number, 
                       setup_data["repo_owner"], repo.name))} for issue in issues]}
