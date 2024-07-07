from tkinter import *

top = Tk()
menubar = Menu(top)

breakfast_menu = Menu(menubar, tearoff=0)
breakfast_menu.add_command(label="Uttapam")
breakfast_menu.add_command(label="Pav Bhaji")
breakfast_menu.add_command(label="Omelette")

menubar.add_cascade(label="Breakfast", menu=breakfast_menu)
menubar.add_command(label="Lunch")
menubar.add_command(label="Dinner")

lunch = Menu(menubar)

top.config(menu=menubar)
top.mainloop()
