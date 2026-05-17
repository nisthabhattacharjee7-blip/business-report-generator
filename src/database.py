import sqlite3

def create_connection():
    con = sqlite3.connect("sales.db")
    return con

def create_table(con):
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sales
                       ( product TEXT,
                        quantity REAL,
                        price REAL,
                        category TEXT)''')
    con.commit()


def insert_data(con, df):
    cursor = con.cursor()
    for index, row in df.iterrows():
        cursor.execute('''
        INSERT INTO sales (product, quantity, price, category)
        VALUES (?, ?, ?, ?)''',(


               row['product'], 
               row['quantity'],
               row['price'],
               row['category']
        ))
    
    
    con.commit()  


def get_total_revenue(con):
    cursor = con.cursor()
    cursor.execute('''
    SELECT SUM(quantity * price) 
    FROM sales''')
    
    total_revenue = cursor.fetchone()
    return total_revenue[0]


def get_category_revenue(con):
    cursor = con.cursor()
    cursor.execute('''
    SELECT category, SUM(quantity * price) 
    FROM sales
    GROUP BY category''')
    
    category_revenue = cursor.fetchall()
    return category_revenue


def  get_top_products(con):
    cursor = con.cursor()
    cursor.execute('''
    SELECT product, 
    SUM(quantity) as total_quantity
    FROM sales
    GROUP BY product
    ORDER BY total_quantity DESC
    ''')
    
    top_products = cursor.fetchall()
    return top_products


def get_category_counts(con):
    cursor = con.cursor()
    cursor.execute('''
    SELECT category,
    COUNT(*) AS total_products
    FROM sales
    GROUP BY category''')
    
    category_counts = cursor.fetchall()
    return category_counts


