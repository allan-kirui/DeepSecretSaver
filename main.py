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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Please provide your username: ")
    username = input()
    print("Hi " + username)
    print("Please provide your password: ")
    password = input()

    valid = is_valid_credentials(username, password)
    if valid:
        deepDarkSecret(username)
    else:
        print("Get outta here")

