#! python3
# selective_copy.py - Program that walks through a folder tree and searches for files with a certain file extension
# (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.

import os
from shutil import copyfile
from pathlib import Path


def search(folder):
    home = str(Path.home())
    newpath = f'{home}\\Desktop\\.pictures_found'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    x = 0
    for root, subfolds, files in os.walk(folder):
        for file in files:
            extensions = ('.jpg', '.jpeg')
            if file.lower().endswith(extensions):
                origin = os.path.join(root, file)  # .lower converts for ex. 'IMG_1217.JPG' to 'img_1217.jpg'
                x += 1  # the first copied file starts with x = 1
                output = f'{newpath}\\pic_{x}.jpg'
                copyfile(origin, output)
    print('All done!')


search(input('Enter a name of a folder (subfolders included) to search for .jpg or .jpeg files '
             'and copy them to the desktop in a folder named ".pictures found".: \n'))
