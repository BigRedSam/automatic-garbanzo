import random
import os
# from PIL import Image, ImageTk
from tkinter import *


root = Tk()


# Create a label to display the result of the roll
result_label = Label(root, text="")
result_label.pack()

# Create a function to roll the dice
def roll_dice():
  # Generate a random number between 1 and 20
  result = random.randint(1, 20)

  # # Create a list of image filenames that correspond to each side of the dice
  # dice_images = [
  #   "d20_side_1.png", "d20_side_2.png", "d20_side_3.png", "d20_side_4.png",
  #   "d20_side_5.png", "d20_side_6.png", "d20_side_7.png", "d20_side_8.png",
  #   "d20_side_9.png", "d20_side_10.png", "d20_side_11.png", "d20_side_12.png",
  #   "d20_side_13.png", "d20_side_14.png", "d20_side_15.png", "d20_side_16.png",
  #   "d20_side_17.png", "d20_side_18.png", "d20_side_19.png", "d20_side_20.png"
  # ]

  # Create an empty list of images
  # images = []

  script_dir=os.path.dirname(__file__)
  # creating filepath
  # image_path = "./"
  image_to_display = "d20_side_" + str(result) + ".png"
  print(image_to_display)
  # PhotoImage(file=image_to_display)
  img = PhotoImage(file=image_to_display)
  Label(
      root,
      image=img
  ).pack()




  # im = Image.open(image_to_display)
  # ph = ImageTk.PhotoImage(im)
  # label = Label(root)
  # label.image = ph
#take result and pull index

  # # Load all of the dice images into the list of images
  # for image in dice_images:
  #   full_image_path = image_path + image
  #   images.append(PhotoImage(file=full_image_path))

  
  # # Create a variable to keep track of the current image being displayed
  # current_image = 0

  # # Create a function to update the image being displayed
  # def update_image():
  #   nonlocal current_image
  #   current_image += 1
  #   if current_image == 20:
  #     current_image = 0
  #   dice_label.config(image=images[current_image])
  #   root.after(100, update_image)

  # # # Create a label to display the dice image
  # dice_label = Label(root, image=image_to_display)
  # dice_label.pack()
  # dice_label.config(image="./d20_side_1.png")
  # dice_label.config(image=image_to_display)
  # Start the animation by calling the update_image function
  # update_image()

  # Update the result label with the final result
  result_label.config(text="Result: " + str(result))

# Create a button to trigger the dice roll
roll_button = Button(root, text="Roll the dice", command=roll_dice)
roll_button.pack()

root.mainloop()
