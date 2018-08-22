#! python3


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def rotate_grid(lst):
    for i in zip(*lst):
        print(' '.join(i))


rotate_grid(grid)

"""OR another solution:
print('\n'.join(map(' '.join, zip(*grid))))
but map() isn't particularly pythonic. I would recommend using list comprehensions instead:

map(f, iterable)
 
is basically equivalent to 

[f(x) for x in iterable]"""
