import tkinter as tk
from tkinter import messagebox

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        
        # Login Frame
        self.login_frame = tk.Frame(root)
        self.login_frame.pack()
        
        self.username_label = tk.Label(self.login_frame, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack()
        
        self.password_label = tk.Label(self.login_frame, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack()
        
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.pack()
        
        # Main Frame
        self.main_frame = tk.Frame(root)
        
        self.add_product_button = tk.Button(self.main_frame, text="Add Product", command=self.add_product)
        self.add_product_button.pack()
        
        self.edit_product_button = tk.Button(self.main_frame, text="Edit Product", command=self.edit_product)
        self.edit_product_button.pack()
        
        self.delete_product_button = tk.Button(self.main_frame, text="Delete Product", command=self.delete_product)
        self.delete_product_button.pack()
        
        self.view_products_button = tk.Button(self.main_frame, text="View Products", command=self.view_products)
        self.view_products_button.pack()
        
        self.low_stock_button = tk.Button(self.main_frame, text="Low Stock Alert", command=self.low_stock_alert)
        self.low_stock_button.pack()
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if authenticate(username, password):
            self.login_frame.pack_forget()
            self.main_frame.pack()
        else:
            messagebox.showerror("Error", "Invalid credentials")
    
    def add_product(self):
        # Code to add product
        pass
    
    def edit_product(self):
        # Code to edit product
        pass
    
    def delete_product(self):
        # Code to delete product
        pass
    
    def view_products(self):
        products = get_products()
        for product in products:
            print(product)
    
    def low_stock_alert(self):
        low_stock_products = low_stock_alert()
        for product in low_stock_products:
            print(product)

root = tk.Tk()
app = InventoryApp(root)
root.mainloop()
