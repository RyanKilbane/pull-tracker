from utils.build_json import build_json

class DummyRepo:
    def __init__(self, issue_name, repo_name):
        self.title = issue_name
        self.repo = repo_name

    def get_issues(self):
        return self.issue

    def title(self):
        return self.title


def test_build_issue_json():
    assert build_json("A Repo") == {"A Repo": {}}

def test_build_issue_json_with_issues():
    assert build_json("A Repo", issues=[DummyRepo("issue1", "A repo"), DummyRepo("issue2", "A repo")]) == {"A Repo": [{"issue_name": "issue1"}, {"issue_name": "issue2"}]}
    