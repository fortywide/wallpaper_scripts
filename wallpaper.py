from PIL import Image
import os

for i in os.listdir("/home/fortywide/Pictures/wallpapers/"):
    if os.path.isdir("/home/fortywide/Pictures/wallpapers/" + i):
        continue
    with Image.open("/home/fortywide/Pictures/wallpapers/" + i) as img:
        width, height = img.size
        print(width, height)
        if width < 3456 or height < 2160:
            os.remove("/home/fortywide/Pictures/wallpapers/" + i)
