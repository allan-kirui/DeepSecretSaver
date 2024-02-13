import os
import sqlite3

def setup_db(database_name):
    connection = sqlite3.connect(database_name)
    cur = connection.cursor()
    cur.execute("CREATE TABLE users (username VARCHAR, password_hash VARCHAR, secret VARCHAR);")
    return connection, cur


def get_tables_and_num_rows(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = cursor.fetchall()
    table_info = {}
    for table_name in table_names:
        table_name = table_name[0]
        cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
        num_rows = cursor.fetchone()[0]
        table_info[table_name] = num_rows

    print(f"The {db} database exists, and it has the following tables and rows:")
    for table, rows in table_info.items():
        print(f"- Table: {table}, Rows: {rows}")
        
        
if __name__ == '__main__':
    uriFile = "file:"
    db = "ppab5.db"
    mode = "?mode=rw"

    try:
        conn = sqlite3.connect((uriFile + db + mode), uri=True)
        cur = conn.cursor()
        # db exists, ask if users wants to delete and recreate it
        # show name of tables and how many rows each have
        get_tables_and_num_rows(cur)

        print("Do you want to delete and recreate the database y for yes, n for no")
        answer = input()
        if answer == "y":
            conn.close()
            os.remove(db)
            conn,curr = setup_db(db)
        elif answer == "n":
            print("Database upheld!")

    except sqlite3.OperationalError:
        # db doesn't exist, ask user if they want to create it
        conn, cursor = setup_db(db)


