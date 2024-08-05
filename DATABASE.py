import sqlite3

def create_db():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    # Create products table
    c.execute('''CREATE TABLE IF NOT EXISTS products
                 (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, price REAL)''')
    # Create users table
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

create_db()
