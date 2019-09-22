from concurrent.futures import ThreadPoolExecutor as tp
import sqlite3 as sql
from github import Github
from db_interface.create_database import database
import os

class Repo:
    def __init__(self, token, owner):
        self.repos = []
        self.git = Github(token)
        self.owner = owner

    def add_repo(self, repo):
        database.add_repo("{}/{}".format(self.owner, repo))

    def poll_database(self):
        repos = []
        for repo in database.get_repos().fetchall():
            repos.append(repo[0])
        return repos

    def get_repos(self):
        saved_repos = self.poll_database()
        with tp(max_workers=5) as executor:
            repo = executor.map(self.git.get_repo, saved_repos)
        return list(repo)

git = Repo(os.environ["git_token"], "ONSDigital")
