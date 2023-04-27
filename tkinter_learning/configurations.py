from tkinter import *
from tkinter import ttk

root = Tk()

button = ttk.Button(root, text = "Hello")
button.grid()
button["text"] = "goodbye"
root.mainloop()