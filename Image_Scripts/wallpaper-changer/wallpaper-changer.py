import schedule
import ctypes
import random
import time
import os

# path to the folder containing the images to be used as wallpapers
rootpath = os.path.dirname(os.path.abspath('wallpaper-changer.py'))
folderpath = os.path.join(rootpath, "wallpapers")
print("Current working directory:", folderpath)
# initializing the list of images
images = []
# creating a list of all the images in the folder
files = os.listdir(folderpath)
for file in files:
    # making sure that the file is an image
    if file.endswith(('.jpg', '.png', '.jpeg')):
        images.append(os.path.join(folderpath, file))

# the relevant flag to be used in the SPIW function
# being initialized in it's integer form
SPI_SETDESKWALLPAPER = SPI_DW = 20


def changeWallpaper():
    # using the random function to ensure that a random image is chosen
    # each time this function gets executed.
    randindex = random.randint(0, (len(images) - 1))
    # now setting the randomly selected image as the desktop wallpaper
    # using the ctypes module's windll api
    ctypes.windll.user32.SystemParametersInfoW(SPI_DW, 0, images[randindex], 0)


# every day at 22:00 time changeWallpaper() is called
schedule.every().day.at("17:00").do(changeWallpaper)

# this loop causes the script to run indefinitely
while True:
    # run all the jobs that are scheduled after every minute
    schedule.run_pending()
    time.sleep(60)
