from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import random


root = Tk()

root.geometry("500x250")
root.title("D20 Roller")

result_label = Label(root, text = "", font = ('Arial', 18))
result_label.pack(padx= 10, pady= 10)


def roll_d20():
    result = random.randint(1, 20)
    img_to_open = f"./d20_side_{result}.png"
    img = Image.open(img_to_open)
    img.show()
    result_label.config(text="Result: " + str(result))



roll_button = Button(root, text="Roll the d20", command=roll_d20)
roll_button.pack(padx=10, pady=5)

root.mainloop()