from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import random

root = Tk()

result_label = Label(root, text="My roll result")
result_label.pack()

Label(root, text='Sammy\'s Famous Dice Roller App', font=(
    'Verdana', 15)).pack(side=TOP, pady=10)


def roll_dice():
    result = random.randint(1, 3)
    if result == 1:
        img_to_open = "./images/cat_a8.gif"
    elif result == 2:
        img_to_open = "./images/cat_a7.gif"
    else:
        img_to_open = "./images/cat_idle.gif"

    load_image = Image.open(img_to_open)
    render = ImageTk.PhotoImage(load_image)
    Button(root, text=result,compound=LEFT).pack()

    img = Label(root, image=render)
    img.image = render
    img.place(x=200, y=60)

    result_label.config(text="Result: " + str(result))


roll_button = Button(root, text="Roll the dice", command=roll_dice)
roll_button.pack()

root.mainloop()