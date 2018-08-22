#! python3
# backup_to_zip.py - Copies an entire folder and its contents into a ZIP file whose filename increments.

import os
import zipfile


def backup_to_zip(folder):
    # Backup the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder)  # make sure folder is absolute

    # Figure out the filename this code should use based on what files already exist.
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'  # For instance 'slozka_1.zip'.
        if not os.path.exists(zip_filename):  # If the ZIP does not exist, break the loop ('number' = 1).
            break
        number += 1  # If the ZIP exists, increment the variable 'number' by 1.
    # The os.path.basename('C:\\fo\\bar\\slozka') returns 'slozka'.
    # The os.path.dirname('C:\\fo\\bar\\slozka') returns 'C:\\fo\\bar'.

    # Create the ZIP file.
    print(f'Creating {zip_filename}...')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')

        # Add the current folder to the ZIP file (in the next iteration, the current folder is its subfolder and so on).
        backup_zip.write(foldername)

        # Add all the FILES in this folder to the ZIP file. One after another.
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'  # For instance 'slozka_'

            # Do NOT backup the backup ZIP files.
            if filename.startswith(new_base) and filename.endswith('.zip'):  # For instance 'slozka_1.zip'
                continue

            # Without this line, only empty folders are added to the ZIP file!
            backup_zip.write(os.path.join(foldername, filename))  # For instance 'C:\\fo\\bar\\slozka\\soubor.txt'.

    backup_zip.close()
    print('Done.')


backup_to_zip('C:\\automate')

"""
The os.walk() function will return three values on each iteration through the loop:
       1) A string of the current folder’s name
       2) A list of strings of the FOLDERS in the current folder
       3) A list of strings of the FILES in the current folder
       4) A string of the first subfolder's name (from_top-down)
       5) A list of strings of the FOLDERS in the subfolder
       6) A list of strings of the FILES in the subfolder and so on...
"""