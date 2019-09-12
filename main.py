from flask import Flask
from add_repo.add_repo import add_repo_blueprint
from track_issues.track_issues import track_issues

app = Flask(__name__)

app.register_blueprint(add_repo_blueprint)
app.register_blueprint(track_issues)

app.run()