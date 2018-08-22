# When a python function is called, the values of the arguments are copied to the parameter variable.


def eggs(some_parameter):
    some_parameter.append('Hello')


spam = [1, 2, 3]
eggs(spam)
print(spam)

# Even though 'spam' and 'some_parameter' lists contain separate references, they both refer to the same list.
