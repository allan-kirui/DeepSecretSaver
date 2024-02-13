import hashlib
import sqlite3
from DatabaseManager import DatabaseManager


class AccountManager:
    def __init__(self):
        self.accounts = {}
        self.database = DatabaseManager()

    def add_account_hash_db(self, username, password):
        """
        adds account to db after hashing the password and returns bool if user was added successfully
        :param username:
        :param password:
        :return bool:
        """
        users = self.get_all_accounts_db()
        if username not in users:
            password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
            self.database.cursor.execute("INSERT INTO users VALUES(?,?,?)", (username, password_hash, "default secret"))
            self.database.connection.commit()
            return True
        else:
            return False

    # returns dictionary of e.g { 'username': ['password','secret']
    def get_all_accounts_db(self):
        """
        returns a dictionary with all users and their account data
        :return dict of users and their account data:
        """
        self.database.cursor.execute("SELECT * FROM users;")
        # columns = [col[0] for col in self.cursor.description]

        users = {row[0]: [row[1], row[2]] for row in self.database.cursor.fetchall()}
        return users

    def connect_to_db(self):
        """
        initiates connection to database
        :return tuple connection & cursor to db:
        """
        conn = sqlite3.connect('ppab5.db')
        cur = conn.cursor()

        return conn, cur

    def is_valid_credentials_db(self, username, password) -> bool:
        """
        checks if credentials entered username & password, match with what was saved in db
        :param username:
        :param password:
        :return bool for match:
        """
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        all_accounts = self.get_all_accounts_db()
        if username in all_accounts.keys() and password_hash == all_accounts[username][0]:
            return True
        else:
            return False

    def get_dark_secret_db(self, username):
        """
        returns user secret from db, it is at index 1 in list
        :param username:
        :return:
        """
        secret = self.get_all_accounts_db()[username][1]
        return secret

    def set_dark_secret_db(self, username):
        """
        sets user secret from db
        :param username:
        """
        print("Please input secret for your account")
        secret = input()
        self.database.cursor.execute(f"UPDATE users SET secret = '{secret}' WHERE username = '{username}';")
        self.database.connection.commit()
        print("Secret saved")
