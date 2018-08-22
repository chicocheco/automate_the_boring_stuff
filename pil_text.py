from PIL import Image, ImageDraw, ImageFont
import os

im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)

# No font and size set {no 4th argument)
draw.text((20, 150), 'Hello', fill='purple')
fontsFolder = 'C:\\Windows\\Fonts'  # e.g. 'Library/Fonts'

# Set a typeface and size
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'Arial.ttf'), 32)
# Use it as a 4th argument in .text method
draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
im.save('text.png')

