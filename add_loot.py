#! python3
# add_loot - Add loot from a dragon to your inventory.

"""
get(key[, default])
Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None,
so that this method never raises a KeyError.

setdefault(key[, default]) - more common to use!! (faster)
If key is in the dictionary, return its value. If not, insert key with a value of default and return default.
default defaults to None.

Al says: setdefault() will do nothing if the key already exists,
you can call it on every iteration of the for loop without a problem.
"""


def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory[item] = inventory.setdefault(item, 0) + 1
        # inv['gold coin'] = 42
        # inv.get('gold coin', 0) = 42
        # inv.setdefault('gold coin', 0) = 42
        # inv.get('dagger', 0) = 0
        # inv.setdefault('dagger', 0) = 0
        # examples of the dict.get(key, default-value) and dict.setdefault(key, default-value) methods:

        # 'dagger' didn't exist yet, assign '0' to the key 'dagger' in the first iteration (to avoid exceptions)
        # 'dagger already existed, add '+1' to its value (second iteration would be 0 + 1)
    return inventory


def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))


inv = {'gold coin': 42, 'rope': 1, 'sword': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby',
               'ruby', 'gold coin', 'sword', 'bow', 'junk ']

inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
