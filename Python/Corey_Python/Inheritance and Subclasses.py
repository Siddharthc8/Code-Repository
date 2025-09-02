class Employee:

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


class Developer (Employee):
    raise_amt = 1.50

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)    #   OR             Useful and easy to handle multiple inheritances
        #Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
            if emp not in self.employees:
                self.employees.append(emp)

    def remove_amp(self, emp):
            if emp in self.employees:
                self.employees.remove(emp)

    def print_emps(self):
            for emp in self.employees:
                print("-->", emp.fullname())


class CEO(Employee):

    def __init__(self, first, last, years = 0):
        super().__init__(first,last, years)     # Here we inherited only the properties we want
        self.years = years


ceo1 = CEO("Dokku", "kumar", 9)
print(ceo1.fullname())

dev1 = Developer('Corey', 'Schafer', 50000, "Python")
dev2 = Developer("Test", "Employee", 60000, "Java")

print(dev1.pay)
dev1.raise_amt = 1.20
dev1.apply_raise()
print(dev1.pay)

print(dev1.email)
print(dev1.prog_lang)

print(dev1)
mgr1 = Manager('Sue', 'Smith', 60000, [dev1])
mgr1.add_emp(dev2)

print(mgr1.email)
mgr1.print_emps()

print(Employee.num_of_emps)

print(isinstance(mgr1, Manager))        # To check if it's an instance of a class (Instance, Class)
print(issubclass(Manager, Employee))    # To check if it's an instance of a class (Subclass, Parent Class)

