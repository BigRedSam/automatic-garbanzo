import random
from tkinter import *


root = Tk()

result_label = Label(root, text="")
result_label.pack()


def roll_d6():
    result = random.randint(1,6)

    result_label.config(text="Result: " + str(result))


roll_button = Button(root, text="Roll the d6", command=roll_d6)
roll_button.pack()

root.mainloop()