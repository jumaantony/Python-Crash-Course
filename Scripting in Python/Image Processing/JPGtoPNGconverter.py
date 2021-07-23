import os
from PIL import Image

# creating the folder to store converted images
if not os.path.exists("coverted_img"):
    os.makedirs("converted_img")

# loop through the images folder
for filename in os.listdir("images"):
    if filename.endswith(".jpg"):
        img = Image.open(os.path.join("./images", filename))
        name = filename[:-4]
        # convert the images to png
        # save the image to converted folder
        img.save(os.path.join("./converted_img", (name + '.png')))
        print("all done")
