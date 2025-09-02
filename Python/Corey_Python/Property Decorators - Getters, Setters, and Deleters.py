class Employee:

    num_of_emps = 0
    raise_amt = 1.10

    def __init__(self, first, last):     # Constructor
        self.first = first
        self.last = last

    @property         # This is used to call an object like an instance without the "()" --> print(e1.email)
    def email(self):
        return f"{self.first}.{self.last}@company.com"

    @property
    def fullname(self):         # Can be called like print(e1.fullname) instead of print(e1.fullname())
        return ("{} {}".format(self.first, self.last))

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(" ")

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None


e1 = Employee('Corey', 'Schafer')
e2 = Employee( "John", "Smith")


e1.first = "Sunny"

print(e1.first)
print(e1.last)
print(e1.email)

e1.fullname = "Sid Chan"
print(e1.fullname)

del e2.fullname
print(e2.fullname)

