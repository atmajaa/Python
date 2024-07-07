#Label box
#We cant make any changes in the label box. A label box can work as a button for event handlings

import tkinter as tk
m = tk.Tk()
greeting = tk.Label(text="This is my first GUI Program", foreground = "yellow", background = "green", width = 50, height = 50)
greeting.pack()
m.mainloop()