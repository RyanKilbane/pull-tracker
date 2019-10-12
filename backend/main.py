import os
import yaml
from backend.setup import InitialSetup
from flask import Flask
from backend.add_repo.add_repo import add_repo_blueprint
from backend.remove_repo.remove_repo import remove_repo_blueprint
from backend.track_issues.track_issues import track_issues
from backend.dashboard.dashboard import dashboard_blueprint
from backend.db_interface.create_database import database
from backend.construct_setup_yaml import setup_data, setup, home
from sqlite3 import OperationalError

database.crate_database()

try:
    database.create_repo_table()
except OperationalError as error:
    print("repo table already exists, skipping")  

try:
    database.create_user_table()
except OperationalError as error:
    print("user table already exists, skipping")
try:
    database.create_admin_table()
except OperationalError as error:
    print(error)
    
if database.count(setup_data["admin_table"]) == 0:
    database.add_admin(setup.create_admins())

app = Flask(__name__, template_folder="pages", static_folder="static")

app.register_blueprint(add_repo_blueprint)
app.register_blueprint(track_issues)
app.register_blueprint(dashboard_blueprint)
app.register_blueprint(remove_repo_blueprint)

app.run(host="0.0.0.0", threaded=True, port=5000)
