all_guests = {'Alice': {'apples': 5, 'pretzels': 12}, 'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}}


def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
        num_brought = num_brought + v.get(item, 0)
    return num_brought


# 'dictinary.items' is a dictionary method to use in for loops to return list-like values to work with
# 'k' is for example Alice and 'v' is for example {'apples': 5, 'pretzels': 12}

# 'inner_dictionary.get' is a dictionary method to check whether there is a key-value or not
# it has two arguments: 'item' is for example 'apples' and '0' is the value to return, if 'apples' does not exist


print('Number of things being brought:')
print(' - Apples ' + str(total_brought(all_guests, 'apples')))
print(' - Cups ' + str(total_brought(all_guests, 'cups')))
print(' - Cakes ' + str(total_brought(all_guests, 'cakes')))
print(' - Ham sandwiches ' + str(total_brought(all_guests, 'ham sandwiches')))
print(' - Apple pies ' + str(total_brought(all_guests, 'apple pies')))