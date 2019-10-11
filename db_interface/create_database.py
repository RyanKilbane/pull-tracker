import sqlite3 as sql
import yaml

class DatabaseSetup:
    def __init__(self, repo_table_name, db_name, user, admin_table_name):
        self.repo_table = repo_table_name
        self.db = db_name
        self.user_table = user
        self.db_connection = None
        self.admin_table = admin_table_name

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

    def create_admin_table(self):
        admin_table = "CREATE TABLE {} (\
            username varchar(256) UNIQUE NOT NULL,\
            email varchar(256),\
            salt varchar(256),\
            password blob,\
            slack_user varchar(256))".format(self.admin_table)
        print("Admin table created")
        print(admin_table)
        cursor = self.db_connection.cursor()
        cursor.execute(admin_table)

    def add_admin(self, admins):
        cursor = self.db_connection.cursor()
        cursor.executemany(f"INSERT INTO {self.admin_table} VALUES (?, ?, ?, ?, ?)", admins)
        self.db_connection.commit()
    
    def add_user(self, new_users):
        cursor = self.db_connection.cursor()
        cursor.executemany("INSERT INTO {} VALUES (?, ?, ?)".format(self.user_table), new_users)
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

    def remove_repos(self, repos):
        cursor = self.db_connection.cursor()
        # cursor.executemany(f"DELETE FROM {self.repo_table} WHERE repo_name=(?)", repos)
        cursor.execute(f"DELETE FROM {self.repo_table} WHERE repo_name=?", (repos,))
        self.db_connection.commit()

with open("setup.yml", "r") as file:
    setup_data = yaml.load(file.read())

database = DatabaseSetup(setup_data["repo_table"], setup_data["database_name"], setup_data["user_table"], setup_data["admin_table"])