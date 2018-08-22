import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]

# pprint.pformat(cats) doesn't print out anything,
# it only returns the exactly same string as seen on line n. 3 after "="

file_obj = open('my_cats.py', 'w')
file_obj.write('cats = ' + pprint.pformat(cats) + '\n')  # this writes the line n. 3 to the .py file
file_obj.close()

