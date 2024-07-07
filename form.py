import tkinter as tk
from tkinter import *
root = tk.Tk()
root.geometry("300x300")
askName = tk.Label(root, text="What is your name?", font="20", foreground = "blue")
askName.pack()
textarea = tk.Text(root, height = 2, width = 170)
textarea.pack()
askReg = tk.Label(root, text="What is your reg number?", font="20", foreground = "blue")
askReg.pack()
textarea1 = tk.Text(root, height = 2, width= 170)
textarea1.pack()
askAddr= tk.Label(root, text="What is your address?", font="20", foreground = "blue")
askAddr.pack()
textarea2 = tk.Text(root, height = 4, width= 170)
textarea2.pack()

def getTexts():
    name = textarea.get("1.0", tk.END).strip()
    regNo = textarea1.get("1.0",tk.END).strip()
    address = textarea2.get("1.0", tk.END).strip()
def click():action.configure(text="submitted")
action = tk.Button(root, text = "Submit", command=getTexts)
action.pack()

root.mainloop()