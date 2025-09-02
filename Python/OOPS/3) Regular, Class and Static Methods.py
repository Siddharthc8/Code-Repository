class Employee:

    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emp += 1        # Like static variables where it is created automatically without intervention

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # Using self takes the value from the created instance
                                                      # Using Employee.raise_amount will take the value from the class itself and not the instance

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str_1. split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



emp1 = Employee("Sid", "Chand", 100000)

emp2 = Employee("Test", "Last", 1000)


print(Employee.raise_amount)
print(emp1.raise_amount)   # Since it is a class variable it is shared across all instances
print(emp2.raise_amount)

Employee.set_raise_amount(1.15)    #(OR)
emp1.set_raise_amount(1.20)


# To use @classmethod decorator as a constructor

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'



new_emp1 = Employee.from_string(emp_str_1)
new_emp2 = Employee.from_string(emp_str_2)

print (new_emp1.email)
print (new_emp1.pay)


import datetime
my_date = datetime.date(2025, 4, 7)

print(Employee.is_work_day(my_date))


