from repos.repo import git
from utils.build_json import build_json
from utils.filter_no_issues import filter_issues
from flask import Blueprint
import json
from github.GithubException import UnknownObjectException

track_issues = Blueprint(name="track_issues", import_name=__name__, url_prefix="/")

@track_issues.route("/pulls")
def issues():
    repos = git.get_repos()
    open_issues = []
    for repo in repos:
        open_issues.append(build_json(repo.name, issues=repo.get_pulls(state="open"), issue_type="pull"))
    print(open_issues)
    # output_issues = filter_issues(open_issues)
    return (json.dumps(open_issues), 200)
