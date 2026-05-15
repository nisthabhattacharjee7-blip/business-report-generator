import sqlite3

def create_connection():
    con = sqlite3.connect("sales.db")
    return con

def create_table(con):
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sales
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       product TEXT NOT NULL,
                       quantity INTEGER NOT NULL,
                       price REAL NOT NULL)''')
    con.commit()


def insert_data(con, df):
    cursor = con.cursor()
    for index, row in df.iterrows():
        cursor.execute('''
        INSERT INTO sales (product, quantity, price)
        VALUES (?, ?, ?)''',(


               row['product'], 
               row['quantity'],
               row['price']

        ))
    
    
    con.commit()  


def get_total_revenue(con):
    cursor = con.cursor()
    cursor.execute('''
    SELECT SUM(quantity * price) 
    FROM sales''')
    
    total_revenue = cursor.fetchone()
    return [0]