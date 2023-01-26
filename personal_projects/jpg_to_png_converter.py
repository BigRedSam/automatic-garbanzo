import os
from PIL import Image

# List of JPG files to convert
jpg_files = [
    "../Pictures/d20_side_1.jpg", "../Pictures/d20_side_2.jpg", "../Pictures/d20_side_3.jpg", "../Pictures/d20_side_4.jpg",
    "../Pictures/d20_side_5.jpg", "../Pictures/d20_side_6.jpg", "../Pictures/d20_side_7.jpg", "../Pictures/d20_side_8.jpg",
    "../Pictures/d20_side_9.jpg", "../Pictures/d20_side_10.jpg", "../Pictures/d20_side_11.jpg", "../Pictures/d20_side_12.jpg",
    "../Pictures/d20_side_13.jpg", "../Pictures/d20_side_14.jpg", "../Pictures/d20_side_15.jpg", "../Pictures/d20_side_16.jpg",
    "../Pictures/d20_side_17.jpg", "../Pictures/d20_side_18.jpg", "../Pictures/d20_side_19.jpg", "../Pictures/d20_side_20.jpg"
  ]

# Loop through the list of JPG files
for file in jpg_files:
    # Open the image file
    with Image.open(file) as im:
        # Get the base name and extension of the file
        base, ext = os.path.splitext(file)
        # Convert the image to a png file
        im.save(base + '.png')
