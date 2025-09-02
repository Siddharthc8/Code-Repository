class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)





emp1 = Employee("Sid", "Chand", 10000)

emp2 = Employee("Test", "Last", 10000)


print(emp1.email)
print(emp2.email)




print(emp1.fullname())  # This can be thought of like the below execution as they are the same

print(Employee.fullname(emp1))