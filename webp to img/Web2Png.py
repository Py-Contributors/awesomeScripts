from PIL import Image
import os

path = input('File path:- ')
files = os.listdir(path)
for filename in files:
    if filename.endswith('webp'): # adding check condition for webp files
        im = Image.open(os.path.join(path, filename)).convert("RGB")
        name = filename.split('.')[0]
        im.save(os.path.join(path, name + '.jpg')
        os.remove(os.path.join(path, filename))
