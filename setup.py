import yaml
import argon2
from argon2 import Argon2Type
import random
import string

class InitialSetup:
    def __init__(self):
        self.database_name = input("What should the name of the database be?: ")
        self.repo_owner = input("Who is the owner of the repos: ")
        self.repo_table = input("What is the name of the repository tabel: ")
        self.user_table = input("What should the user table be called: ")
        self.git_token = input("Where is the Git token located (this should be an environment variable): ")
        self.salting = string.ascii_letters + "0123456789"
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
            admin_name = input("Enter admin user name: ")
            admin_email = input("Enter admin email: ")
            admin_salt = ''.join(random.choice(self.salting) for i in range(30))
            admin_password = argon2.argon2_hash(password=input("Enter admin password: "), salt=admin_salt, argon_type=0)
            print(type(admin_password))
            print(admin_password)
            print(str(admin_password))
            admins.append((admin_name, admin_email, admin_salt, admin_password))
            if input("Add another (Y/N): ") != "Y":
                break
        return admins
    
    def write_yaml(self):
        with open("setup.yml", "w") as file:
            yaml.dump(self.output_dict, file, default_flow_style=False)
        return self
