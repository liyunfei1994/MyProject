import os
import re


image_dir = "E:/PycharmProjects/pictures/6400_crop"

for root, dirs, files in os.walk(image_dir):
    print("files", files)
    for name in files:
        if int(re.sub('[.jpg]', '', name))%2 != 0:
            os.remove(os.path.join(image_dir, name))
