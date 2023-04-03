import random
from tkinter import *

def roll_d6():
    result = random.randint(1,6)
    
    result_label.config(text="Result: " + str(result))

root = Tk()

result_label = Label(root, text="")
result_label.pack()

roll_button = Button(root, text="Roll the d6", command=roll_d6)
roll_button.pack()

root.mainloop()