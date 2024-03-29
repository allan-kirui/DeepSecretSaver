import pyautogui
from AccountManager import AccountManager


def get_username_password():
    """
    gets username and password from user
    :return tuple of username and password:
    """
    print("Please provide your username or enter q to quit: ")
    username = input()
    check_quit(username)
    print("Hi " + username)
    print("Please provide your password or enter q to quit: ")
    password = pyautogui.password(text='Enter your password:', title='Password', mask='*')
    check_quit(password)

    return username, password


def login(accountManager, username, password):
    """
    logs in verified users, and allows them to perform various actions
    :param accountManager:
    :param username:
    :param password:
    """
    valid = accountManager.is_valid_credentials_db(username, password.strip())
    if valid:
        print("Welcome to Deep Secret Saver "+ username + "!")
        while True:
            print("******************")
            print(" # To retreive secret please enter 'r'")
            print("# To modify secret please enter 'm'")
            print("To logout please enter 'o'")
            print("******************")
            action = input()

            if action == 'r':
                secret = accountManager.get_dark_secret_db(username)
                print(username + "'s secret is " + secret)
            elif action == 'm':
                accountManager.set_dark_secret_db(username)
            elif action == "o":
                print("Successfully logged out")
                break
    else:
        print("Invalid username or password")


def create_account(accountManager, username, password):
    """
    creates accounts for new users
    :param accountManager:
    :param username:
    :param password:
    """
    addedAccSuccess = accountManager.add_account_hash_db(username, password)
    if addedAccSuccess:
        print("Account Created")
        print("Please login to your account")
    else:
        print("Invalid username or password")


def check_quit(keyword):
    """
    quits the app if appropriate keyword is input by user
    :param keyword:
    """
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

    accountManager.database.connection.close()

