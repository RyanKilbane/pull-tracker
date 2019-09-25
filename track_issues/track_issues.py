from repos.repo import git
from utils.build_json import build_json_threads
from utils.filter_no_issues import filter_issues
from flask import Blueprint
import json
from concurrent.futures import ProcessPoolExecutor

track_issues = Blueprint(name="track_issues", import_name=__name__, url_prefix="/")

@track_issues.route("/pulls")
def issues():
    repos = git.get_repos()
    with ProcessPoolExecutor(max_workers=3) as Executor:
        x = Executor.map(build_json_threads, repos)
    open_issues = list(x)
    return (json.dumps(open_issues), 200)
