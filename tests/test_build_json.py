from utils.build_json import build_json
class DummyRepo:
    def __init__(self, issue, name):
        self.issue = issue
        self.name = name
    def get_issues(self):
        return self.issue
    def get_name(self):
        return self.name

dummy = DummyRepo("an issue", "a repo")
def test_build_issue_json():
    assert build_json("issue") == {"issue": {}}

def test_build_json_repos():
    repo_names = ["repo1", "repo2", "repo3"]
    assert build_json("issues", issues="", repos=repo_names) == {"issues": {"repo1": [], "repo2": [], "repo3": []}}
