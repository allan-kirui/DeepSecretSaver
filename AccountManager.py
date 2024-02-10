from Account import Account
import hashlib
import yaml
class AccountManager:
    def __init__(self):
        self.accounts = {}
        self.load_accounts()

    def add_account(self, username, password):
        if username not in self.accounts:
            account = Account(username, password)
            self.accounts[account.username] = account
            return True
        else:
            return False

    def add_account_hash(self, username, password):
        if username not in self.accounts:
            account = Account(username, hashlib.sha256(password.encode('utf-8')).hexdigest())
            self.accounts[account.username] = account
            return True
        else:
            return False

    def get_account(self, username):
        if username in self.accounts:
            return self.accounts[username]

    def get_all_accounts(self):
        accounts = self.accounts
        all_accounts = []
        for username, account in accounts.items():
            all_accounts.append({'username': username, 'password': account.get_password()})
        return all_accounts

    def load_accounts(self):
        with open('credentials.yaml', 'r') as file:
            credentials = yaml.safe_load(file)
        for acc in credentials:
            self.add_account(acc['username'], acc['password'])

    def save_accounts(self):
        with open('credentials.yaml', 'w') as file:
            yaml.safe_dump(self.get_all_accounts(), file)

    def is_valid_credentials(self, username, password) -> bool:
        pwd = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if username in self.accounts and pwd == self.accounts[username].get_password():
            return True
        else:
            return False
