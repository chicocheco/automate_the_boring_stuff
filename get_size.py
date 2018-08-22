#! python3

import os

total_size = 0
for filename in os.listdir('C:\\Python\\ABS'):
    if not os.path.isfile(os.path.join('C:\\Python\\ABS', filename)):
        continue
    # skips folders
    total_size += os.path.getsize(os.path.join('C:\\Python\\ABS', filename))

print(total_size)
