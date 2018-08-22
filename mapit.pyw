#! python3
# mapit.pyw - Launches a map in the browser using an address from the command line or clipboard.
# If there are no command line arguments, the program will assume the address is stored on the clipboard.

"""
The sys.argv variable stores a list of the program’s filename and command line arguments.
If this list has more than just the filename in it, then len(sys.argv) evaluates to an integer greater than 1,
meaning that command line arguments have indeed been provided.
"""

import pyperclip
import sys
import webbrowser

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])  # Create just one very long string without the program name (sys.argv[0]).
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
