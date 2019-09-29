from flask import render_template, request, Blueprint
from sqlite3 import IntegrityError
from repos.repo import git
import json
from db_interface.create_database import database

remove_repo = add_repo_blueprint = Blueprint(name="remove_repo",import_name=__name__, url_prefix="/")

@remove_repo.route("/remove")
def remove_repo():
    pass