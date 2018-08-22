import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}  # prepares an empty dictionary for the following for loop
for character in message:  # iterates over each character, an empty space included
    count.setdefault(character, 0)  # sets up a key-value to 0 for every found character
    count[character] += 1  # adds up 1 (firstly to the 0 value)

pprint.pprint(count)
