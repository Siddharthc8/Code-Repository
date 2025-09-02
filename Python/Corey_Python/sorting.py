
import operator
from operator import attrgetter
li = [9,1,8,2,7,3,6,4,5]
s_li = sorted(li)
print("Original list :",li)
print("Sorted list :", s_li)

# Reverse
r_li = sorted(li, reverse=True)
li.sort(reverse=True)
print("Reverse method :",li)
print("Reverse sort  :", s_li)

tup = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup)
print(s_tup)                 # Output is a list

di = {'name': 'Corey', 'job': 'programming', 'age': "fifty", 'os': "Mac"}
s_di = sorted(di.items(), key = lambda x: x[0])            # "Keys", "Values" and "Items" for both
print(s_di)

neg_li = [-6, -5, -4, 1, 2, 3]
s_neg_li = sorted(neg_li, key = abs)                        #    OR     s_neg_li = sorted(neg_li, key = lambda x: abs(x))
print(s_neg_li)

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
       return (f"{self.name}, {self.age}, ${self.salary}")        # .format(self.name, self.age, self.salary)


e1 = Employee("Carl", 37, 70000)
e2 = Employee("Sarah", 29, 80000)
e3 = Employee("John", 43, 90000)

employees = [e1, e2, e3]                                           # List of employees

def e_sort(emp):
    return emp.name

s_employees = sorted(employees, key = e_sort)
# OR
# s_employees = sorted(employees, key = lambda x: x.age )        # To avoid using the function, you can use the following line
# OR
# s_employees = sorted(employees, key =attrgetter("age"))        # This requires library "operator" and the method "attrgetter"
print(s_employees)
