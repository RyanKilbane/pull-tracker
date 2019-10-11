import requests
from ..repos.repo import git
import os
def get_reviewers(pull_number, owner, repo):
    reviews = requests.get(f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers", headers={'Authorization': 'token {}'.format(os.environ['git_token'])})
    return reviews.json()
