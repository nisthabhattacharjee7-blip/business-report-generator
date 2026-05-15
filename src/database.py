import sqlite3

def create_connection():
    con = sqlite3.connect("sales.db")
    return con

def create_table(con):
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sales
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       product_name TEXT NOT NULL,
                       quantity INTEGER NOT NULL,
                       price REAL NOT NULL)''')
    con.commit()