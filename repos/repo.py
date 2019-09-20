from concurrent.futures import ThreadPoolExecutor as tp
import sqlite3 as sql
from sqlite3 import IntegrityError
from github import Github
from db_interface.create_database import database
import os

class Repo:
    def __init__(self, token):
        self.repos = set(["ONSDigital/takeon-ui", "ONSDigital/takeon-business-layer", "ONSDigital/takeon-persistence-layer",
                      "ONSDigital/takeon-response-persistence-lambda"])
        self.git = Github(token)
    
    def add_repo(self, repo):
        database.add_repo("ONSDigital/{}".format(repo))
        self.repos.add("ONSDigital/{}".format(repo))

    def get_repos(self):
        with tp(max_workers=5) as executor:
            repo = executor.map(self.git.get_repo, self.repos)
        return list(repo)

git = Repo(os.environ["git_token"])
