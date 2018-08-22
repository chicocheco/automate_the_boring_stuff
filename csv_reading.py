
import csv

example_file = open('example.csv')
example_reader = csv.reader(example_file)

for row in example_reader:
    print(f'Row #{str(example_reader.line_num)} {str(row)}')

example_file.close()
