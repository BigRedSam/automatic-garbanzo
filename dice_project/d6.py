import random
from tkinter import *

def roll_d6():
    result = random.randint(1,6)
    
    result_label.config(text="Result: " + str(result))

root = Tk()
root.geometry("150x75")
root.title("D6 roller")

result_label = Label(root, text="", font=("Arial", 16))
result_label.pack(padx=10, pady=5)

roll_button = Button(root, text="Roll the d6", command=roll_d6)
roll_button.pack(padx=10, pady=5)

root.mainloop()