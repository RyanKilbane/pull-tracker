from concurrent.futures import ThreadPoolExecutor as tp
from github import Github
import os

class Repo:
    def __init__(self, token):
        self.repos = set(["ONSDigital/takeon-ui", "ONSDigital/takeon-business-layer", "ONSDigital/takeon-persistence-layer",
                      "ONSDigital/takeon-response-persistence-lambda"])
        self.git = Github(token)
    
    def add_repo(self, repo):
        self.repos.add("ONSDigital/{}".format(repo))

    def get_repos(self):
        with tp(max_workers=5) as executor:
            repo = executor.map(self.git.get_repo, self.repos)
        return list(repo)

git = Repo(os.environ["git_token"])
