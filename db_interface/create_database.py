import sqlite3 as sql

class DatabaseSetup:
    def __init__(self, repo_table_name, db_name):
        self.repo_table = repo_table_name
        self.db = db_name
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
    
    def add_repo(self, new_repo):
        add_repo = "INSERT INTO {} VALUES ('{}')".format(self.repo_table, new_repo)
        cursor = self.db_connection.cursor()
        cursor.execute(add_repo)
        self.db_connection.commit()      

database = DatabaseSetup("repos", "repos_db")