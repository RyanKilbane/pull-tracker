class DummyRepo:
    def __init__(self, issue_name, repo_name, issue_number):
        self.title = issue_name
        self.name = repo_name
        self.number = issue_number
    def get_issues(self):
        return self.issue

    def title(self):
        return self.title
