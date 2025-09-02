class Employee:                   # Operator Overloading
                                  # __init__ is called dunder init
    num_of_emps = 0
    raise_amt = 1.10     # If a Class Variable should be accessed it can be done through by using the "self.variable"
                            # def apply_raise(self):
                            #     self.pay = int(self.pay * self.raise_amount) OR (self.pay * Employee.raise_amount)

    def __init__(self, first, last, pay):     # Constructor
        first = first[0].upper() + first[1:]
        self.first = first
        last = last[0].upper() + last[1:]
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1    # Can't change cuz we like to keep it constant and there is no use to change it

    def fullname(self):
        return ("{} {}".format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    """ __repr__ and __str__ are only for representing the contents of a Class
    When "print(e1)" where e1 is an instance is tried to be printed it will first try to access the __str__ followed by __repr__
    """

    def __repr__(self):                       # Unambiguous representation of an object
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):                        # Readable representation of an object
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

e1 = Employee('Corey', 'Schafer', 50000)
e2 = Employee( "John", "Smith", 60000)

print(e1)
print(repr(e1))
print(str(e1))
print(e1.__repr__())

print(e1 + e2)

print("test".__len__())