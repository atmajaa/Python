#Write a python program to display 3 labels that represents traffic lights and their name
import tkinter as tk
m = tk.Tk()
greeting = tk.Label(text="red", foreground = "red", background = "red", width = 20, height = 20)
greeting1 = tk.Label(text="yellow", foreground = "yellow", background = "yellow", width = 20, height = 20)
greeting2 = tk.Label(text="green", foreground = "green", background = "green", width = 20, height = 20)
greeting.pack()
greeting1.pack()
greeting2.pack()
m.mainloop()

#From the tkinter library we have to create an object for the Tk class. This object provides the basic route 
#for other gui objects such as label, textbox etc. 
#From the tk object we can call any of the member with dot operator. For eg tk.label. Whatever the GUI object we are 
#creating to display the object we need the pack function.
#The loop canvas will execute with the help of mainloop function. 