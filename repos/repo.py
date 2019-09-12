from concurrent.futures import ThreadPoolExecutor as tp
from github import Github

class Repo:
    def __init__(self):
        self.repos = ["ONSDigital/takeon-ui", "ONSDigital/takeon-business-layer", "ONSDigital/takeon-persistence-layer",
                      "ONSDigital/takeon-response-persistence-lambda"]
        self.git = Github()
    
    def add_repo(self, repo):
        self.repos.append("ONSDigital/{}".format(repo))

    def get_repos(self):
        with tp(max_workers=3) as executor:
            repo = executor.map(self.git.get_repo, self.repos)
        return list(repo)

git = Repo()
