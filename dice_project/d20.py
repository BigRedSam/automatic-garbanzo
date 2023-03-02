from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import random


root = Tk()

result_label = Label(root, text = "")
result_label.pack()

def roll_d20():
    result = random.randint(1, 20)
    
    if result == 1:
        img_to_open = "./dice_project/d20_side_1.png"
    elif result == 2:
        img_to_open = "./dice_project/d20_side_2.png"
    elif result == 3:
        img_to_open = "./dice_project/d20_side_3.png"
    elif result == 4:
        img_to_open = "./dice_project/d20_side_4.png"
    elif result == 5:
        img_to_open = "./dice_project/d20_side_5.png"
    elif result == 6:
        img_to_open = "./dice_project/d20_side_6.png"
    elif result == 7:
        img_to_open = "./dice_project/d20_side_7.png"
    elif result == 8:
        img_to_open = "./dice_project/d20_side_8.png"
    elif result == 9:
        img_to_open = "./dice_project/d20_side_9.png"
    elif result == 10:
        img_to_open = "./dice_project/d20_side_10.png"
    elif result == 11:
        img_to_open = "./dice_project/d20_side_11.png"
    elif result == 12:
        img_to_open = "./dice_project/d20_side_12.png"
    elif result == 13:
        img_to_open = "./dice_project/d20_side_13.png"
    elif result == 14:
        img_to_open = "./dice_project/d20_side_14.png"
    elif result == 15:
        img_to_open = "./dice_project/d20_side_15.png"
    elif result == 16:
        img_to_open = "./dice_project/d20_side_16.png"
    elif result == 17:
        img_to_open = "./dice_project/d20_side_17.png"
    elif result == 18:
        img_to_open = "./dice_project/d20_side_18.png"
    elif result == 19:
        img_to_open = "./dice_project/d20_side_19.png"
    elif result == 20:
        img_to_open = "./dice_project/d20_side_20.png"
    
    load_image = Image.open(img_to_open)
    render = ImageTk.PhotoImage(load_image)
    Button(root, text=result,compound=LEFT).pack()

    img = Label(root, image=render)
    img.image = render
    img.place(x=200, y=60)
    
    result_label.config(text="Result: " + str(result))


roll_button = Button(root, text="Roll the d20", command=roll_d20)
roll_button.pack()

root.mainloop()