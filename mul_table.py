#! python3
# mul_table.py - Multiplies an input number by a number in range from 1 to 10


def mul_table(y):
    print([(x, x * y) for x in range(1, 11)])


print('Multiplication table for number:')
y = int(input())
mul_table(y)
