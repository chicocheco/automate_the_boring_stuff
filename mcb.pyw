#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.

"""
Usage:      py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
            py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
            py.exe mcb.pyw list - Loads all keywords to clipboard.
            py.exe mcb.pyw delete <keyword> - Deletes a single keyword from the DB (shelve, dictionary).
            py.exe mcb.pyw delete - Deletes all items from the DB (shelve, dictionary).

.pyw extension is used for not showing (poping up) the terminal when the program is executed.

The sys.argv variable stores a LIST of the program’s filename and command line arguments.
That means that the command line arguments have index 1 and more (sys.argv[0] is ALWAYS the filename).
"""

import pyperclip
import shelve
import sys

mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3:  # Two arguments are inputed by an user.
    if sys.argv[1].lower() == 'save':  # 'save <keyword>'
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':  # 'delete <keyword>'
        mcb_shelf.pop(sys.argv[2])  # .pop is a dictionary method. If the <keyword> is in the dictionary, remove it.

elif len(sys.argv) == 2:  # One argument is inputed.
    if sys.argv[1].lower() == 'delete':  # 'delete'
        mcb_shelf.clear()  # .clear is a dictionary method. Removes all items from the dictionary.
    elif sys.argv[1].lower() == 'list':  # 'list'
        pyperclip.copy(str(list(mcb_shelf.keys())))  # list(dict.keys()) get a list of saved keywords of the dict.
    elif sys.argv[1] in mcb_shelf:  # '<keyword>'
        pyperclip.copy(mcb_shelf[sys.argv[1]])  # Copy the value of the keyword to the clipboard.


mcb_shelf.close()
