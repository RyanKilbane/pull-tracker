from concurrent.futures import ThreadPoolExecutor as tp
import sqlite3 as sql
from github import Github
from github.GithubException import UnknownObjectException
from ..db_interface.create_database import database
from ..construct_setup_yaml import setup_data
import os
import yaml

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
        with tp(max_workers=8) as executor:
            repo = executor.map(self.git.get_repo, saved_repos)
        repo_list = self.build_list(repo)
        return repo_list

    def remove_repo(self, repo):
        database.remove_repos("{}/{}".format(self.owner, repo))

    def build_list(self, repos):
        output_list = []
        try:
            for repo in repos:
                print(repo)
                output_list.append(repo)
        except UnknownObjectException as error:
            print("A repo returned 404, this likely means that the repo doesn't exist")
        return output_list

git = Repo(os.environ[setup_data["git_token"]], setup_data["repo_owner"])
