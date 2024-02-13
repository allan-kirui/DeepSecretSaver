import sqlite3

def setup_db(database_name):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE users (username VARCHAR, password_hash VARCHAR)")
    return connection, cursor

if __name__ == '__main__':
    uriFile = "file:"
    db = "ppab5.db"
    mode = "?mode=rw"


    try:
        conn = sqlite3.connect((uriFile + db + mode), uri=True)
        # db exists, ask if users wants to delete and recreate it
        # show name of tables and how many rows each have

    except sqlite3.OperationalError:
        # db doesn't exist, ask user if they want to create it
        conn, cursor = setup_db(db)


