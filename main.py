from AccountManager import AccountManager
import hashlib
def get_username_password():
    print("Please provide your username or enter q to quit: ")
    username = input()
    check_quit(username)
    print("Hi " + username)
    print("Please provide your password or enter q to quit: ")
    password = input()
    check_quit(password)

    return username, password


def login(accountManager, username, password):
    valid = accountManager.is_valid_credentials(username, password.strip())
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


def create_account(accountManager, username, password):
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


