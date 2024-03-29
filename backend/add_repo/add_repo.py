from flask import render_template, request, Blueprint
from sqlite3 import IntegrityError
from ..repos.repo import git
import json
from ..db_interface.create_database import database

add_repo_blueprint = Blueprint(name="add_repo",import_name=__name__, url_prefix="/")

@add_repo_blueprint.route("/add", methods=["POST"])
def add_repo():
    new_repo = request.args.get("repo")
    if new_repo == "":
        return (json.dumps({"message": "No repo passed"}), 200)
    try:
        git.add_repo(new_repo)
        return (json.dumps({"message": "Repo added"}), 200)
    except IntegrityError as error:
        return (json.dumps({"message": "Repo already exists"}), 200)

@add_repo_blueprint.route("/add", methods=["GET"])
def get_page():
    tracked_repos = database.get_repos()
    repos = []
    for repo in tracked_repos:
        repos.append(repo[0])
    print(repos)
    return render_template("add_repo.html", tracked_repos=repos)
