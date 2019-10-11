from backend.utils.filter_no_issues import filter_issues

def test_filter_returns_empty_dict():
    issues = {"A repo": []}
    assert filter_issues(issues) == {}

def test_filter():
    issues = {"A repo": [{"pull_name": "a pull"}, 
                         {"pull_name": "another pull"}],
             "Another repo":[{"pull_name": "a pull"}]}
    assert sorted(filter_issues(issues)) == sorted(issues)

def test_filter_one_repo_has_issue():
    issues = {"A repo": [],
             "Another repo":[{"pull_name": "a pull"}]}
    assert filter_issues(issues) == {"Another repo":[{"pull_name": "a pull"}]}
