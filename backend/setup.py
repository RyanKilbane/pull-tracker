import yaml
import random
import string
import os
from .users.users import Users
from getpass import getpass

class InitialSetup:
    def __init__(self, home_dir):
        if not os.path.isfile(os.path.join(home_dir, "setup.yml")):
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
                            "git_token": self.git_token,
                            "admin_table": "admins"}
        return self

    def create_admins(self):
        admins = []
        while True:
            admin_user = Users(input("Enter admin user name: "), input("Enter admin email: "), getpass("Add password: "), input("Slack username (leave blank to not include): "))
            admin_salt = admin_user.build_salt()
            hashed_pass = admin_user.hash_password(admin_salt)
            admins.append(admin_user.create_insert_tuple(admin_salt, hashed_pass))
            if input("Add another (Y/N): ") != "Y":
                break
        return admins
    
    def write_yaml(self, home_dir):
        print(os.path.join(home_dir, "setup.yml"))
        with open(os.path.join(home_dir, "setup.yml"), "w") as file:
            yaml.dump(self.output_dict, file, default_flow_style=False)
        return self
