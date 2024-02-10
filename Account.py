import hashlib
class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.secret = "default secret"

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_dark_secret(self):
        return self.secret

    def set_dark_secret(self):
        print("Please input secret for your account")
        self.secret = input()
        print("Secret saved")