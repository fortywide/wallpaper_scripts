from PIL import Image
import tkinter as tk
import os
from pathlib import Path

root = tk.Tk()
root.withdraw() 
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

relative_path = "~/Pictures/wallpapers/"
wallpaper_folder = Path(relative_path).expanduser()

for i in os.listdir(wallpaper_folder):
    if os.path.isdir(wallpaper_folder / i):
        continue
    with Image.open(wallpaper_folder / i) as img:
        width, height = img.size
        print(width, height, wallpaper_folder / i)
        if width < screen_width or height < screen_height:
            os.remove(wallpaper_folder / i)
