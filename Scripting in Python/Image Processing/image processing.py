# this is customization of an images to improve the look and feel of the image
from PIL import Image, ImageFilter

img = Image.open('./images/pikachu.jpg')

"""
print(img)  # prints the image information
print(img.format)  # prints the image format
print(img.size)  # prints the image size
print(img.mode)  # prints the mode of the image
print(dir(img))
"""

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("./processed_image/blur.png", 'png')

filtered_img2 = img.filter(ImageFilter.SMOOTH)
filtered_img2.save("./processed_image/smooth.png", 'png')

filtered_img3 = img.convert('L')
filtered_img3.save("./processed_image/L.png", 'png')
filtered_img3.show()  # shows the image

rotate = filtered_img3.rotate(70)  # rotates the image 90 degrees
rotate.save("./processed_image/rotate.png", 'png')
rotate.show()

img2 = Image.open('./images/bulbasaur.jpg')
img2.thumbnail((100, 100))
img2.save("./processed_image/thumbnail.png", 'png')
img2.show()