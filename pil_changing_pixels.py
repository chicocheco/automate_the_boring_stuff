from PIL import Image
from PIL import ImageColor

im = Image.new('RGBA', (100, 100))
print(im.getpixel((0, 0)))

# top half is light gray
for x in range(100):
    for y in range(50):
        im.putpixel((x, y), (210, 210, 210))

# second half is dark gray
for x in range(100):
    for y in range(50, 100):
        im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))

print(im.getpixel((0, 0)))
print(im.getpixel((0, 50)))

im.save('put_pixel.png')
