# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def is_valid_credentials(username, password) -> bool:
    if username == 'admin' and password == '<PASSWORD>':
        return True
    else:
        return False

def deepDarkSecret(username):
    secret = {"admin": "I run the world"}
    print(username + " deep dark secret is " + secret["admin"])

def check_quit(keyword):
    if keyword == 'q':
        print("Goodbye")
        exit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    while True:
        print("Please provide your username or enter q to quit: ")
        username = input()
        check_quit(username)
        print("Hi " + username)
        print("Please provide your password or enter q to quit: ")
        password = input()
        check_quit(password)

        valid = is_valid_credentials(username, password)
        if valid:
            deepDarkSecret(username)
        else:
            print("Invalid username or password")

