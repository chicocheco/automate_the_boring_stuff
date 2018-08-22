# ! python3
# pil_res_add_logo.py - Resizes all images in current working directory to fit in a 300x300 square,
# and adds catlogo_res.png to the lower-right corner.

"""
Notes:
    The original catlogo.png was too big. Reduced from 808 x 768 to 142 x 150 using the same method as in the if-else
    clause used here but resized to half size (not 300, but 150 on at least one side).
    In .resize() method was added a usage of an optional resample filter: Image.LANCZOS.

    Scaling:
    Important is to know how to scale the length of the other side with the one being resized:
    side1 = (new_side1 / side2) * side1)
"""

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo_res.png'

logo_im = Image.open(LOGO_FILENAME)

logo_width, logo_height = logo_im.size

os.makedirs('with_logo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')) or filename == LOGO_FILENAME:
        continue

    im = Image.open(filename)
    width, height = im.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image.
        print(f'Resizing {filename}...')

        im = im.resize((width, height), Image.LANCZOS)

    print(f'Adding logo to {filename}...')
    # Image.paste(pasted_image, (coordinates of the top-left corner), pasted_image again to add transparency)
    im.paste(logo_im, (width - logo_width, height - logo_height), logo_im)

    # Save changes.
    im.save(os.path.join('with_logo', filename))
