import os
import pathlib
import shutil

os.makedirs('renamed', exist_ok=True)
for filename in os.listdir('.'):
    if filename.lower().endswith('.mp4'):
        base = os.path.splitext(filename)[0]
        print()
        numbering = base[-4:].strip('p. ')
        new_base = numbering.zfill(2) + ' ' + base[:-4].strip()
        renamed_filename = new_base + os.path.splitext(filename)[1]
        print(os.path.abspath(filename))
        print(os.path.abspath(f'.\\renamed\\{renamed_filename}'))
        shutil.move(os.path.abspath(filename), f'.\\renamed\\{renamed_filename}')

