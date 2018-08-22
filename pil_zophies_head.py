from PIL import Image

cat_im = Image.open('zophie.png')
face_im = Image.open('cropped.png')

cat_im_width, cat_im_height = cat_im.size
face_im_width, face_im_height = face_im.size

cat_copy_two = cat_im.copy()

print(f'\nThe image has this width: {str(cat_im_width)} and this height: {str(cat_im_height)}')
print(f'The pasting image has this width: {str(face_im_width)} and this height: {str(face_im_height)}\n')

# Top-left corner is (0, 0)
# Outer loop for moving from left to right.
count = 0
for from_left in range(0, cat_im_width, face_im_width):
    # Inner loop for moving from top to down.
    print(f'Pasting the top-left corner at {from_left} pixels far from the left edge:')
    for from_top in range(0, cat_im_height, face_im_height):
        print(from_left, from_top)
        cat_copy_two.paste(face_im, (from_left, from_top))
    count += 1
    print(f'The column number {count} is finished.\n')


cat_copy_two.save('tiled.png')
