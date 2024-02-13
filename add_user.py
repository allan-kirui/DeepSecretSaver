import hashlib
import sqlite3
import pyautogui

if __name__ == '__main__':
    # Connect to DB
    conn = sqlite3.connect('ppab5.db')
    cur = conn.cursor()

    # check if username is unique
    users = dict(cur.execute("SELECT * FROM users;"))
    user_input = input('Enter your usename:')
    while user_input in users.keys():
        user_input = input('Username exists. Please enter a unique usename')

    password = pyautogui.password(text='Enter your password:', title='Password', mask='*')
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    cur.execute("INSERT INTO users VALUES(?,?)", (user_input, password_hash))
    conn.commit()


