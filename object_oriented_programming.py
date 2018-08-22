# Python Object-Oriented Programming by Corey Schafer


class Employee:

    num_of_emps = 0         # Class variable
    raise_amt = 1.04        # Instance variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# Class variable:
print(Employee.num_of_emps)
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
print(Employee.num_of_emps)

# Static method (independent but logically related method):
import datetime
my_date = datetime.date(2018, 4, 26)
print(Employee.is_workday(my_date))

# Class method:
Employee.set_raise_amt(1.05)  # is equal to Employee.raise_amt = 1.05
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# Another class method:
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'
# this method does this: first, last, pay = emp_str.split('-')
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
