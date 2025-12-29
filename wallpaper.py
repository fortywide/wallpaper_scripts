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

files = [path for path in wallpaper_folder.rglob('*') if path.is_file()]

for i in files:
    with Image.open(i) as img:
        width, height = img.size
        print(width, height, i)
        if width < screen_width or height < screen_height:
            os.remove(i)
            continue
        if i.suffix != '.png':
            img.save(i.parent / (i.stem + '.png'))
            os.remove(i)
