def low_stock_alert(threshold=10):
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('SELECT * FROM products WHERE quantity <= ?', (threshold,))
    low_stock_products = c.fetchall()
    conn.close()
    return low_stock_products

def sales_summary():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('SELECT * FROM sales')
    sales = c.fetchall()
    conn.close()
    return sales
