from tkinter import *
top = Tk()
top.geometry("200x250")
lbl = Label(top,text = "A list of fav countries...")
listbox = Listbox(top)
listbox.insert(1,"Japan")
listbox.insert(2,"South Korea")
listbox.insert(1,"Vietnam")
listbox.insert(1,"USA")
lbl.pack()
listbox.pack()
top.mainloop()
