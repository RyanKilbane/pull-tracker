from utils.build_json import build_json
from tests.unit_tests.dummy_repo import DummyRepo

def test_build_issue_json():
    assert build_json("A Repo") == {"A Repo": {}}

def test_build_issue_json_with_issues():
    assert build_json("A Repo", issues=[DummyRepo("issue1", "A repo"), DummyRepo("issue2", "A repo")]) == {"A Repo": [{"issue_name": "issue1"}, {"issue_name": "issue2"}]}
    