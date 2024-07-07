from tkinter import *
import tkinter as tk
from tkinter import ttk
data = [
    (1, "Mammal", "Lion", "Active"),
    (2, "Bird", "Peacock", "Active"),
    (3, "Reptile", "Crocodile", "Inactive"),
]
root =tk.Tk()
root.title("VanVihar Information Table")

tree = ttk.Treeview(root, columns=("Serial Number","Category", "Name","Status"), show="headings")
tree.heading("Serial Number", text = "Serial Number")
tree.heading("Category", text = "Category")
tree.heading("Name", text = "Name")
tree.heading("Status", text = "Status")

tree.column("Serial Number", width=100)
tree.column("Category", width=100)
tree.column("Name", width=100)
tree.column("Status", width=100)

for item in data:
    tree.insert("", tk.END, values=item)

tree.pack(pady=20, padx=20)

root.mainloop()

