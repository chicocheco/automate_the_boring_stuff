# Python Object-Oriented Programming by Corey Schafer


class Employee:

    raise_amt = 1.04        # Instance variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(repr(emp_1))  # dunder __repr__ specifies how to reproduce the instance
print(emp_1)  # if __str__ is specified, it overrides __repr__ method output by default

print(emp_1 + emp_2)  # __add__ method changes the way how '+' is handled

print(len(emp_1))  # __len__ is changed to use len() implicitly on Employee.fullname()


