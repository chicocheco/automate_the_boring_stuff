import os

for folderName, subfolders, filenames in os.walk('C:\\Python'):
    print(f'The current folder is {folderName}')

    for subfolder in subfolders:
        print(f'SUBFOLDER OF {folderName}: {subfolder}')
    for filename in filenames:
        print(f'FILE INSIDE {folderName}:  {filename}')

# The os.walk() function will return three values on each iteration through the loop:
    # A string of the current folder’s name
    # A list of strings of the folders in the current folder
    # A list of strings of the files in the current folder
