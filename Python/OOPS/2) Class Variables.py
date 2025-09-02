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



emp1 = Employee("Sid", "Chand", 100000)

emp2 = Employee("Test", "Last", 1000)


emp1.raise_amount = 1.10

print(Employee.raise_amount)
print(emp1.raise_amount)   # Since it is a class variable it is shared across all instances
print(emp2.raise_amount)

emp1.apply_raise()

print(emp1.pay)
print(emp2.pay)

print(Employee.num_of_emp)


print(emp1.__dict__)
print(Employee.__dict__)

