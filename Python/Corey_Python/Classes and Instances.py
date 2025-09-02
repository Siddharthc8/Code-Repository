class Employee:

    num_of_emps = 0
    raise_amt = 1.04     # If a Class Variable should be accessed it can be done through by using the "self.variable"
                            # def apply_raise(self):
                            #     self.pay = int(self.pay * self.raise_amount) OR (self.pay * Employee.raise_amount)

    def __init__(self, first, last, pay):     # Constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1    # Can't change cuz we like to keep it constant and there is no use to change it

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amt) # e1.raise_amount = 'x' does not affect "self.pay"   ..OR..
      # self.pay = int(self.pay * self.raise_amount)     # e1.raise_amount = 'x' affects "self.pay"

    def fullname(self):
        return ("{} {}".format(self.first, self.last))


e1 = Employee('Corey', 'Schafer', 50000)
e2 = Employee( "John", "Smith", 60000)

print(e1.fullname())         # OR      # Understand that the variable or instance is passed to self in the function so
print(Employee.fullname(e1))           # passing self in the function is important

print(e1.pay)               # Prints the pay
e1.apply_raise()            # Instance followed by the method/fn
print(e1.pay)

# Accessing methods for class variables
print(Employee.raise_amt)
print(e1.raise_amt)

print(Employee.__dict__)           # Displays all the attributes of the Class

e1.raise_amt = 1.05             # Changing the value only for that instance "e1"
print(e1.__dict__)                 # Displays all the attributes of the Instance

Employee.raise_amt = 1.05       # Changing the value for the whole class

print(Employee.num_of_emps)        # Everytime the method __init__ is used it increments the value of "num_of_emps"

e1.raise_amt = 1.50
e1.apply_raise()            # Instance followed by the method/fn
print(e1.pay)