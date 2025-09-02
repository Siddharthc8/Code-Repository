nums = [1, 2, 3, 4, 5, 6, 7, 8,9, 10]

# I want 'n' for each 'n' in nums
my_list = []
for n in nums:
    my_list. append (n)
print(my_list)
# Using LC function
new_list = [n for n in nums]
print(new_list)
# Using lambda function
list1 = list(map(lambda n: n*n, nums))
print(list1)


# Condition is n if n is even
my_list = []
for n in nums:
    if n%2 == 0:
        my_list. append (n)
print(my_list)
# Using LC
result = [n for n in nums if n%2 == 0]
# Using filter
res = list(filter(lambda n: n%2 == 0, nums))
print(res)

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list2 = []
for letter in 'abcd':
    for num in range (4):
        my_list2.append((letter, num))
print(my_list2)

# Using LC
my_list3 = [(letter,num) for letter in "abcd" for num in range(4)]

# Dictionary Comprehension

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

print(list(zip(names, heros)))          # Kinda stitches these two values to a tuple in a list

# Creates a dictionary with name as the key and hero as the value
my_dict = {}
for name, hero in zip(names, heros) :
    my_dict [name] = hero
print(my_dict)

# Using Dictionary comprehension
my_dict1 = {name: hero for name, hero in zip(names, heros)}
print(my_dict1)

# Add Constraints
my_dict2 = {name: hero for name, hero in zip(names, heros) if name!= "Wade"}
print(my_dict2)

# Set Comprehensions
numbers = [ 1, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7, 7, 8, 9]
my_set = set()
for number in numbers:
    my_set.add(number)
print(my_set)

# Using Set Comprehension
my_set = {number for number in numbers}
print(my_set)

# Generator Expressions
# I want to yield 'n*n' for each
list_22 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def gen_func(numb):
    for n in numb:
        yield n*n                # Yield is for returning int


my_gen = gen_func(list_22)
for i in my_gen:
    print(i, end = " ")

# Generator expression for the above code
print("")
my_gen1 = (n*n for n in list_22)
for i in my_gen1:
    print(i, end = " ")