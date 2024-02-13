import sqlite3
import yaml
import os


class DatabaseManager:
    def __init__(self):
        self.configs = None
        self.database_name = None
        self.get_configs()
        self.set_database_name()
        self.connection = None
        self.cursor = None
        self.setup_db()

    def get_configs(self):
        """
        gets configs from yaml file
        """
        with open('config.yaml', 'r') as ymlfile:
            self.configs = yaml.safe_load(ymlfile)

    def get_database_name(self):
        """
        returns database name
        :return:
        """
        return self.database_name

    def set_database_name(self):
        """
        sets database name as read from yaml file
        """
        self.database_name = self.configs[0]['db-name']

    def get_tables_and_num_rows(self):
        """
        prints tables and number of rows from the db
        """
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        table_names = self.cursor.fetchall()
        table_info = {}
        for table_name in table_names:
            table_name = table_name[0]
            self.cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
            num_rows = self.cursor.fetchone()[0]
            table_info[table_name] = num_rows

        print(f"The {self.database_name} database exists, and it has the following tables and rows:")
        for table, rows in table_info.items():
            print(f"- Table: {table}, Rows: {rows}")

    def setup_db(self):
        """
        sets up the database and performs appropriate actions if it already exists
        """
        uriFile = "file:"
        mode = "?mode=rw"

        try:
            self.connection = sqlite3.connect((uriFile + self.database_name + mode), uri=True)
            self.cursor = self.connection .cursor()
            # db exists, ask if users wants to delete and recreate it
            # show name of tables and how many rows each have
            self.get_tables_and_num_rows()

            print("Do you want to delete and recreate the database y for yes, n for no")
            answer = input()
            if answer == "y":
                self.connection.close()
                os.remove(self.database_name)
                self.create_db()
            elif answer == "n":
                print("Database upheld!")

        except sqlite3.OperationalError:
            # db doesn't exist, ask user if they want to create it
            self.create_db()

    def create_db(self):
        """
        connects to db and creates tables
        """
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE users (username VARCHAR, password_hash VARCHAR, secret VARCHAR);")
        self.connection.commit()
