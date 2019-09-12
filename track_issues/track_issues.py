from repos.repo import git
from flask import Blueprint

track_issues = Blueprint(name="track_issues",import_name=__name__, url_prefix="/")

@track_issues.route("/issues")
def issues():
    repos = git.get_repos()
    open_issues = {"issue": {}}
    for repo in repos:
        open_issues["issue"] = repo.name
        open.append(list(repo.get_issues(state="open")))
    print(open_issues)
    return (open_issues, 200)