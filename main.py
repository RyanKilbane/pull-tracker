import os
from setup import InitialSetup

if not os.path.isfile("setup.yml"):
    setup = InitialSetup().make_dict().write_yaml()

from flask import Flask
from add_repo.add_repo import add_repo_blueprint
from track_issues.track_issues import track_issues
from dashboard.dashboard import dashboard_blueprint
from db_interface.create_database import database
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
    
if os.path.isfile("setup.yml"):
    database.add_admin(setup.create_admins())

app = Flask(__name__, template_folder="pages", static_folder="static")

app.register_blueprint(add_repo_blueprint)
app.register_blueprint(track_issues)
app.register_blueprint(dashboard_blueprint)

app.run(host="0.0.0.0", threaded=True)
