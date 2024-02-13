import hashlib
import sqlite3

if __name__ == '__main__':
    # Connect to DB
    conn = sqlite3.connect('ppab5.db')
    cur = conn.cursor()

    # check if username is unique
    users = dict(cur.execute("SELECT * FROM users;"))
    user_input = input('Enter your usename')
    while user_input in users.keys():
        user_input = input('Username exists. Please enter a unique usename')

    password = input('Enter your password')
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    users = dict(cur.execute("SELECT * FROM users;"))


    cur.execute("INSERT INTO users VALUES(?,?)", (user_input, password_hash))
    conn.commit()


