import tkinter as tk
ws = tk.Tk()
ws.geometry("550x550")
greeting = tk.Label(ws, text="Enter name", foreground="black", background="white", width=20, height=2)
greeting.pack()
text_area = tk.Text(ws, height=60, width=60)
text_area.pack()
ws.mainloop()
