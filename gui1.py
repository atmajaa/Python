from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("300x200")
messagebox.showinfo("University","Tomorrow is holiday")
messagebox.showwarning("Class Teacher","Submit the assignments on time")
messagebox.showerror("Student", "I am not able to solve it")
messagebox.askquestion("Parents","Why do you have short attendance. Do you want to sit at home?")
messagebox.askokcancel("Friends", "Will you join for coffee?")
messagebox.askyesno("Results","Are you promoted for next class")
messagebox.askretrycancel("Online courses","Do you want to join assignments?")
root.mainloop(())