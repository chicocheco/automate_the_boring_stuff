#! python3
# print_table.py - prints out a list of lists in right-justified columns.

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


# nyx version
def print_table(table):
    col_widths = []

    # find the longest string in each sublist for determining width of each column
    for col in table:
        col_widths.append(max([len(x) for x in col]))

        # for loop iterates over lists in the list
        # and searches for the longest string in each list in the list to save its length

    for row in zip(*table):
        print(" ".join([x.rjust(col_widths[i]) for i, x in enumerate(row)]))

        # zip(*list) for unpacking a list of lists. it merges index[0] of each sublist and creates a list of
        # all values which previously had index[0].
        # For example (apples, Alice, dogs) then it merges all values with index[1], index[2] and so on

        # " ".join('apples'.rjust(8))...
        # " ".join adds an empty space to join items "x" from the list
        # enumerate() iterates over indices ('i') and items ('x') of a list, it returns a tuple
        # for ex.: list(enumerate(table_data[0])) is evaluated to [(0, 'apples'), (1, 'oranges'), (2, 'cherries')...]


print_table(table_data)


"""
--------------------------------------------------------
zip() is to iterate over two lists in parallel. Example:

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for a, b in zip(alist, blist):
    print a, b
    
a1 b1
a2 b2
a3 b3
----------------------------------------------------------------------------------------
enamurate() is to iterate over items and indices in a list using enumerate. For example:

alist = ['a1', 'a2', 'a3']

for i, a in enumerate(alist):
    print i, a
    
0 a1
1 a2
2 a3

-OR-

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for i, (a, b) in enumerate(zip(alist, blist)):
    print i, a, b
    
0 a1 b1
1 a2 b2
2 a3 b3
----------------------------------------------------------------------------------------


What I wanted from the function:

print(table[0][0].rjust(col_widths[0]), table[1][0].rjust(col_widths[1]), table[2][0].rjust(col_widths[2]))
print(table[0][1].rjust(col_widths[0]), table[1][1].rjust(col_widths[1]), table[2][1].rjust(col_widths[2]))
print(table[0][2].rjust(col_widths[0]), table[1][2].rjust(col_widths[1]), table[2][2].rjust(col_widths[2]))
print(table[0][3].rjust(col_widths[0]), table[1][3].rjust(col_widths[1]), table[2][3].rjust(col_widths[2]))

"""

