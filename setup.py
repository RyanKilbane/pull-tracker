import yaml

class InitialSetup:
    def __init__(self):
        self.database_name = input("What should the name of the database be?: ")
        self.repo_owner = input("Who is the owner of the repos: ")
        self.repo_table = input("What is the name of the repository tabel: ")
        self.user_table = input("What should the user table be called: ")
        self.git_token = input("Where is the Git token located (this should be an environment variable): ")
        self.output_dict = None

    def make_dict(self):
        self.output_dict = {"database_name": self.database_name,
                            "repo_owner": self.repo_owner,
                            "repo_table": self.repo_table,
                            "user_table": self.user_table,
                            "git_token": self.git_token}
        return self
    
    def write_yaml(self):
        with open("setup.yml", "w") as file:
            yaml.dump(self.output_dict, file, default_flow_style=False)
