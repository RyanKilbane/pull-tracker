from flask import Flask
from add_repo.add_repo import add_repo_blueprint

app = Flask(__name__)

app.register_blueprint(add_repo_blueprint)

app.run()