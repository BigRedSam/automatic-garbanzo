from PIL import Image, ImageFilter, ImageDraw, ImageFont

image = Image.open('d20_side_1.png')

# rotated_image = image.rotate(90, expand=True)
# rotated_image.save('rotate_left.png')

# rotated_image = image.rotate(-90, expand=True)
# rotated_image.save('rotate_right.png')

# rotated_image = image.rotate(180, expand=True)
# rotated_image.save('upside_down.png')

# smaller_image = image.resize((500,500))
# smaller_image.save('smaller_img.png')

# width = image.width
# height = image.height

# print(width, height)

# half_height = int(height / 2)
# half_width = int(width / 2)

# half_size = image.resize((half_width, half_height))
# half_size.show()
# half_size.save('d20_side1_half_size.png')

# image.thumbnail((250,250))
# image.save('d20side1thumbnail.png')

# flip_vertical = image.transpose(Image.FLIP_LEFT_RIGHT)
# flip_vertical.show()

# flip_horizontal = image.transpose(Image.FLIP_TOP_BOTTOM)
# flip_horizontal.show()

# embossed_image = image.filter(ImageFilter.EMBOSS)
# embossed_image.show()

# blurred_image = image.filter(ImageFilter.BLUR)
# blurred_image.show()

# contour_image = image.filter(ImageFilter.CONTOUR)
# contour_image.show()

# img_draw = ImageDraw.Draw(image)
# # the list of points are the coordinates of the top left corner X and Y 
# # and the bottom right corner X and Y 
# img_draw.rectangle([900, 620, 1100, 720], outline='black')

# font = ImageFont.truetype('DejaVuSans.ttf', 50)
# img_draw.text([780,780], 'read/write head', fill='purple', font=font)

# image.show()