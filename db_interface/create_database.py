import sqlite3 as sql
import yaml

class DatabaseSetup:
    def __init__(self, repo_table_name, db_name, user):
        self.repo_table = repo_table_name
        self.db = db_name
        self.user_table = user
        self.db_connection = None

    def crate_database(self):
        try:
            connect = sql.connect(self.db, check_same_thread=False)
            self.db_connection = connect
        except Exception as e:
            print(e)
            connect.close()
    
    def create_repo_table(self):
        repo_table = "CREATE TABLE {} (\
                      repo_name varchar(256) UNIQUE)".format(self.repo_table)
        cursor = self.db_connection.cursor()
        cursor.execute(repo_table)

    def create_user_table(self):
        user_table = "CREATE TABLE {} (\
                     username varchar(256) UNIQUE NOT NULL,\
                     slack_name varchar(256) UNIQUE NOT NULL,    \
                     last_messaged int)".format(self.user_table)
        cursor = self.db_connection.cursor()
        cursor.execute(user_table)
    
    def add_user(self, new_users):
        cursor = self.db_connection.cursor()
        cursor.executemany("INSERT INTO {} VALUES (?, ?, ?)", new_users).format(self.user_table)
        self.db_connection.commit()

    def add_repo(self, new_repo):
        add_repo = "INSERT INTO {} VALUES ('{}')".format(self.repo_table, new_repo)
        cursor = self.db_connection.cursor()
        cursor.execute(add_repo)
        self.db_connection.commit() 

    def get_repos(self):
        get_repos = "SELECT * FROM {}".format(self.repo_table)
        cursor = self.db_connection.cursor()
        return cursor.execute(get_repos)

with open("setup.yml", "r") as file:
    setup_data = yaml.load(file.read())

database = DatabaseSetup(setup_data["repo_table"], setup_data["database_name"], setup_data["user_table"])