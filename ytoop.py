# more OOP fundamentals. (class variables vs instance variables)

class Employee:

    # class variable accessed via the class (Employee)
    num_of_emps = 0
    # instance variable accessed via the instance of the class (self)
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # the iterator to count employees accessed via class (Employee)
        Employee.num_of_emps += 1

    # accessed via the instance (self)
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # accessed via the instance (self)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# initially there are no employees
print Employee.num_of_emps

# added 7 employees
emp_1 = Employee('Jake', 'Ross', 65000)
emp_2 = Employee('Sara', 'Skiest', 75000)
emp_1 = Employee('Jack', 'Rose', 45000)
emp_2 = Employee('Sara Ann', 'Skiesto', 85000)
emp_1 = Employee('Jason', 'Roth', 95000)
emp_2 = Employee('Sally', 'Skillsaw', 175000)
emp_1 = Employee('James', 'Rosello', 265000)

# updated the count with 7 new employees
print Employee.num_of_emps
