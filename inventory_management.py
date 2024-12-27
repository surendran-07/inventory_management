import tkinter as tk
from tkinter import messagebox

# User authentication
users = {"admin": "password123"}  # Example user credentials

def authenticate(username, password):
    return users.get(username) == password

# Inventory data
inventory = {}

# GUI Functions
def login():
    username = username_entry.get()
    password = password_entry.get()
    if authenticate(username, password):
        login_frame.pack_forget()
        inventory_frame.pack()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def add_product():
    product = product_name_entry.get()
    quantity = product_quantity_entry.get()
    try:
        quantity = int(quantity)
        if product in inventory:
            inventory[product] += quantity
        else:
            inventory[product] = quantity
        messagebox.showinfo("Success", f"Added {quantity} of {product}.")
        product_name_entry.delete(0, tk.END)
        product_quantity_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Quantity must be an integer.")

def edit_product():
    product = product_name_entry.get()
    quantity = product_quantity_entry.get()
    try:
        quantity = int(quantity)
        if product in inventory:
            inventory[product] = quantity
            messagebox.showinfo("Success", f"Updated {product} to {quantity}.")
        else:
            messagebox.showerror("Error", "Product not found.")
        product_name_entry.delete(0, tk.END)
        product_quantity_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Quantity must be an integer.")

def delete_product():
    product = product_name_entry.get()
    if product in inventory:
        del inventory[product]
        messagebox.showinfo("Success", f"Deleted {product}.")
    else:
        messagebox.showerror("Error", "Product not found.")
    product_name_entry.delete(0, tk.END)

def generate_report():
    report = "Inventory Report:\n" + "\n".join(f"{product}: {quantity}" for product, quantity in inventory.items())
    if not inventory:
        report += "\nInventory is empty."
    messagebox.showinfo("Inventory Report", report)

# GUI Setup
app = tk.Tk()
app.title("Inventory Manager")

# Login frame
login_frame = tk.Frame(app)
login_frame.pack()

tk.Label(login_frame, text="Username:").grid(row=0, column=0)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1)

tk.Label(login_frame, text="Password:").grid(row=1, column=0)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1)

tk.Button(login_frame, text="Login", command=login).grid(row=2, column=0, columnspan=2)

# Inventory frame
inventory_frame = tk.Frame(app)

product_name_label = tk.Label(inventory_frame, text="Product Name:")
product_name_label.grid(row=0, column=0)
product_name_entry = tk.Entry(inventory_frame)
product_name_entry.grid(row=0, column=1)

product_quantity_label = tk.Label(inventory_frame, text="Quantity:")
product_quantity_label.grid(row=1, column=0)
product_quantity_entry = tk.Entry(inventory_frame)
product_quantity_entry.grid(row=1, column=1)

tk.Button(inventory_frame, text="Add Product", command=add_product).grid(row=2, column=0)
tk.Button(inventory_frame, text="Edit Product", command=edit_product).grid(row=2, column=1)
tk.Button(inventory_frame, text="Delete Product", command=delete_product).grid(row=3, column=0)
tk.Button(inventory_frame, text="Generate Report", command=generate_report).grid(row=3, column=1)

# Start application
app.mainloop()
