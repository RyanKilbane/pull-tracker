class DummyRepo:
    def __init__(self, issue_name, repo_name):
        self.title = issue_name
        self.repo = repo_name

    def get_issues(self):
        return self.issue

    def title(self):
        return self.title
