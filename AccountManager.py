from Account import Account
class AccountManager:
    def __init__(self):
        self.accounts = {
            'admin': Account('admin', 'pass'),
            'student': Account('student', 'stud')
                         }

    def add_account(self, username, password):
        if username not in self.accounts:
            account = Account(username, password)
            self.accounts[account.username] = account
            return True
        else:
            return False

    def get_account(self, username):
        if username in self.accounts:
            return self.accounts[username]

    def is_valid_credentials(self, username, password) -> bool:
        if username in self.accounts and password == self.accounts[username].get_password():
            return True
        else:
            return False
