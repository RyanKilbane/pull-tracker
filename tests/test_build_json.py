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
    assert build_json("A Repo") == {"A Repo": {}}

def test_build_issue_json_with_issues():
    assert build_json("A Repo", issues=["issue1", "issue2"]) == {"A Repo": [{"issue_name": "issue1"}, {"issue_name": "issue2"}]}