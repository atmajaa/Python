from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("300x300")
w = Label(root, text = "Message Box", font = "20")
w.pack()
messagebox.showinfo("University","Tomorrow is a holiday")
messagebox.showwarning("Class teacher","Submit the assignment on time")
messagebox.showerror("Student","I am not able to solve it")
messagebox.askquestion("First Text", "Kya tum VIT Bhopal se hoo?")
messagebox.askokcancel("Ask","Will you date me?")
messagebox.askretrycancel("Genuine question", "Can I lick you?")

