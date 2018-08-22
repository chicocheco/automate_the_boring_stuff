guests = {'Alice': 2, 'Bob': 4, 'Carol': 8}
other_guests = {'Alice': 1, 'Bob': 1, 'Carol': 2}

all_guests = {**guests, **other_guests}

for k, v in all_guests.items():
    print(k)
    print(v)

