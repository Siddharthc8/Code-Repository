class Employee:

    num_of_emps = 0
    raise_amt = 1.04     # If a Class Variable should be accessed it can be done through by using the "self.variable"
                            # def apply_raise(self):
                            #     self.pay = int(self.pay * self.raise_amount) OR (self.pay * Employee.raise_amount)

    def __init__(self, first, last, pay):
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

    @classmethod                         # This line is called a decorator
    def set_raise_amt(cls, amount):      # Take in "cls" for "self"
        cls.raise_amt = amount     # X   # Changes the value for the entire class including all other instances as well
                                         # Behaves more like a clas variable
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split(',')      # Mentioned the split criterion
        return cls(first, last, pay)    # X    # Calling/Returning the function from within one of the functions of the class
                                        # X      # "cls" can be used instead of the actual class name, more like "self"

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



e1 = Employee('Corey', 'Schafer', 50000)
e2 = Employee( "John", "Smith", 60000)

Employee.set_raise_amt(1.06)
#      OR                          # Sets the new raise_amt value to the entire class and all instances
e1.set_raise_amt(1.05)             # This method does not make sense

print(Employee.raise_amt)
print(e1.raise_amt)
print(e2.raise_amt)

e_str_1 = 'John,Doe,70000'
e_str_2 = 'Steve,Smith,30000'
e_str_3 = 'Jane,Doe,90000'

new_e1 = Employee.from_string(e_str_1)
new_e2 = Employee.from_string(e_str_2)
new_e3 = Employee.from_string(e_str_3)

print(new_e1.pay)

import datetime
my_date = datetime.date(2024,7,6)
print(Employee.is_workday(my_date))