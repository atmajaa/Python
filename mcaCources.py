#Write a python program to display the list of courses mca students have complete. 
#The list box should have vertical and horizontal scrollbar. Whatever the course a user
#selects the subject teacher name must be reflected in the textbox available near to
#the listbox

from tkinter import *
top = Tk()
top.geometry("200x250")
lbl = Label(top,text = "A list of fav countries...")
listbox = Listbox(top)
listbox.insert(1,"OOP in Java")
listbox.insert(2,"Advanced Operating System")
listbox.insert(1,"Android Programming")
listbox.insert(1,"Information Security")
lbl.pack()
listbox.pack()
top.mainloop()
