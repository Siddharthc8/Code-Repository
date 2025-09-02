class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay) :
        self.first = first
        self. last = last
        self.email = first + '.' + last +'@email.com'
        self.pay = pay

    def fullname (self) :
        return '{} {}'. format(self.first, self. last)

    def apply_raise(self) :
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):

    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang) :
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print("-->", emp.fullname())



dev_1 = Developer ('Corey', 'Schafer', 50000, "Python")
dev_2 = Developer ('Test', 'Employee', 60000, "Java")
print(dev_1. email)
print (dev_2.email)

mgr1 = Manager("Sue", "Smith", 90000, [dev_1])
mgr1.add_employee(dev_2)
mgr1.remove_employee(dev_1)

print(mgr1.email)

mgr1.print_employees()


print(isinstance(mgr1, Employee))