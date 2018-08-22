#! python3


def comma_code(lst):
    text1 = []
    for i in range(0, len(lst) - 2):
        text1.append(lst[i])
    text1.append(lst[-2] + ' and ' + lst[-1] + '.')
    first = text1[0]
    text1[0] = first.capitalize()
    text2 = ', '.join(text1)
    print(text2)


spam = ['apples', 'bananas', 'tofu', 'cats']
my_pets = ['Zophie', 'Pooka', 'Fat-tail', 'Niky', 'Elvis', 'Max', 'Bob']
comma_code(spam)
comma_code(my_pets)


# using f-strings:
def comma_code2(lst):
    if len(lst) == 1:
        return lst[0]
    print(f'{lst[0].capitalize()}, {", ".join(lst[1:-1])}, and {lst[-1]}.')
    # first part is separated by {} and capitalizes only the value [0]
    # second part is separated by {} and joins only the values [1:-1] ... the second index is not included
    # third part is separated by {} again and refers only the last value [-1]


comma_code2(spam)
comma_code2(my_pets)
