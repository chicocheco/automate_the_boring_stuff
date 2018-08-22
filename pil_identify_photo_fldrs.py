#! python3 #
# pil_identify_photo_fldrs.py - Checks whether a folder has

import os

from PIL import Image

broken_img_files = []
for foldername, subfolders, filenames in os.walk('C:\\'):
    num_photo_files = 0
    num_non_photo_files = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not filename.lower().endswith('.jpg') or filename.lower().endswith('.png'):
            num_non_photo_files += 1
            continue  # skip to next filename

        path = os.path.join(foldername, filename)
        try:
            # Open image file using Pillow.
            im = Image.open(path)
            width, height = im.size
        except OSError:
            broken_img_files.append(path)
            continue

        # Check if width & height are larger than 500.
        if width > 500 and height > 500:
            # Image is large enough to be considered a photo.
            num_photo_files += 1
        else:
            # Image is too small to be a photo.
            num_non_photo_files += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
    if num_photo_files > num_non_photo_files:
        print('A possible photo folder: ' + os.path.abspath(foldername))

if broken_img_files:
    while True:
        answer = input('\nSome image files were not possible to open. Do you want to see them? (Y/N): ').lower()
        if answer == 'y':
            for image in broken_img_files:
                print(image)
            break
        elif answer == 'n':
            break
