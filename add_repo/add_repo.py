from flask import render_template, request, Blueprint
from sqlite3 import IntegrityError
from repos.repo import git
import json

add_repo_blueprint = Blueprint(name="add_repo",import_name=__name__, url_prefix="/")

@add_repo_blueprint.route("/add", methods=["POST"])
def add_repo():
    new_repo = request.args.get("repo")
    if isinstance(new_repo, type(None)):
        return ("No repo passed", 400)
    try:
        git.add_repo(new_repo)
        print(git.repos)
        return ("Added", 200)
    except IntegrityError as error:
        return (json.dumps({"error": "Repo already exists"}), 500)

@add_repo_blueprint.route("/add", methods=["GET"])
def get_page():
    return render_template("add_repo.html")
