import hashlib
import sqlite3


class AccountManager:
    def __init__(self):
        self.accounts = {}
        self.connection, self.cursor = self.connect_to_db()

    def add_account_hash_db(self, username, password):
        users = self.get_all_accounts_db()
        if username not in users:
            password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
            self.cursor.execute("INSERT INTO users VALUES(?,?,?)", (username, password_hash, "default secret"))
            self.connection.commit()
            return True
        else:
            return False

    def get_account(self, username):
        if username in self.accounts:
            return self.accounts[username]

    # returns dictionary of e.g { 'username': ['password','secret']
    def get_all_accounts_db(self):
        self.cursor.execute("SELECT * FROM users;")
        # columns = [col[0] for col in self.cursor.description]

        users = {row[0]: [row[1], row[2]] for row in self.cursor.fetchall()}
        return users

    def connect_to_db(self):
        conn = sqlite3.connect('ppab5.db')
        cur = conn.cursor()

        return conn, cur

    # checks if credentials entered, match with what was saved
    def is_valid_credentials_db(self, username, password) -> bool:
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        all_accounts = self.get_all_accounts_db()
        if username in all_accounts.keys() and password_hash == all_accounts[username][0]:
            return True
        else:
            return False

    # returns user secret from db, it is at index 1 in list
    def get_dark_secret_db(self, username):
        secret = self.get_all_accounts_db()[username][1]
        return secret

    def set_dark_secret_db(self, username):
        print("Please input secret for your account")
        secret = input()
        self.cursor.execute(f"UPDATE users SET secret = '{secret}' WHERE username = '{username}';")
        self.connection.commit()
        print("Secret saved")
