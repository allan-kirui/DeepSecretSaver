# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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

def get_username_password():
    print("Please provide your username or enter q to quit: ")
    username = input()
    check_quit(username)
    print("Hi " + username)
    print("Please provide your password or enter q to quit: ")
    password = input()
    check_quit(password)

    return username, password

def login(accountManager,username, password):
    valid = accountManager.is_valid_credentials(username, password)
    if valid:
        print("Welcome to Deep Secret Saver "+ accountManager.get_account(username).get_username() + "!")
        while True:
            print("******************")
            print("To retreive secret please enter 'r'")
            print("To modify secret please enter 'm'")
            print("To logout please enter 'o'")
            print("******************")
            action = input()

            if action == 'r':
                secret = accountManager.get_account(username).get_dark_secret()
                print(accountManager.get_account(username).get_username() + "'s secret is " + secret)
            elif action == 'm':
                accountManager.get_account(username).set_dark_secret()
            elif action == "o":
                print("Successfully logged out")
                break
    else:
        print("Invalid username or password")

def create_account(accountManager,username, password):
    addedAccSuccess = accountManager.add_account(username, password)
    if addedAccSuccess:
        print("Account Created")
        print("Please login to your account")
    else:
        print("Invalid username or password")
def check_quit(keyword):
    if keyword == 'q':
        print("Goodbye")
        exit()


if __name__ == '__main__':
    accountManager = AccountManager()
    while True:
        print("******************")
        print("Welcome to Deep Secret Saver")
        print("To login please input 'l'")
        print("To create an account please input 'c'")
        print("To quit please input 'q'")
        print("******************")
        startAction = input()

        if startAction == 'l':
            # LOG IN
            username, password = get_username_password()
            login(accountManager, username, password)

        elif startAction == 'c':
            # CREATE ACCOUNT
            username, password = get_username_password()
            create_account(accountManager, username, password)

        elif startAction == 'q':
            print("Goodbye")
            break


