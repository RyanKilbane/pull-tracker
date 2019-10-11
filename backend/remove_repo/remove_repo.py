from flask import render_template, request, Blueprint
from sqlite3 import IntegrityError
from ..repos.repo import git
import json
from ..db_interface.create_database import database

remove_repo = remove_repo_blueprint = Blueprint(name="remove_repo",import_name=__name__, url_prefix="/")

@remove_repo_blueprint.route("/remove", methods=["POST"])
def add_repo():
    new_repo = request.args.get("repo")
    if new_repo == "":
        return (json.dumps({"message": "No repo passed"}), 200)
    try:
        git.remove_repo(new_repo)
        return (json.dumps({"message": "Repo removed"}), 200)
    except IntegrityError as error:
        return (json.dumps({"message": "Repo already exists"}), 200)

@remove_repo_blueprint.route("/remove", methods=["GET"])
def get_page():
    tracked_repos = database.get_repos()
    repos = []
    for repo in tracked_repos:
        repos.append(repo[0])
    print(repos)
    return render_template("remove_repo.html", tracked_repos=repos)