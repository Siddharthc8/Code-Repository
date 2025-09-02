person = {'name': 'Jenn', 'age': 23}

sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old. '
print (sentence)

sentence = "My name is {} and I am {} years old.".format(person['name'], person['age'])
print(sentence)

sentence = 'My name is {0} and I am {1} years old. {0} is my first name.'.format (person['name'], person['age'])
print(sentence)

sentence = "My name is {0[name]} and I am {0[age]} years old.".format(person)
print(sentence)                    # See the difference when you pass it with the "**" in the following example

sentence = "My name is {name} and I am {age} years old.".format(**person)
print(sentence)                    # Don't have to mention the place of the .format argument

li = ['Jenn', 23]
sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(li)
print (sentence)

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Jack', '33')
print(sentence)
sentence = "My name is {0.name} and I am {0.age} years old".format(p1)

sentence = 'My name is {name} and I am {age} years old. '.format(name='Jenn', age='30')
print(sentence)

for i in range(1, 11):                               # Zero padding my result
    sentence = 'The value is {:02}'.format(i)        # The ":" is used to indicate formatting
    print(sentence)                                  # "0" is the pad, and "2" is the no of places in result, prints(01)
# Output for {:02} = The value is 01
# Output for {:03} = The value is 001

pi = 3.14159265
sentence = "Pi is equal to {:.3f}".format(pi)      # .2f is the no of places after the decimal place
print(sentence)                                    # Result is in 2 decimal places after the dot
# Output = Pi is equal to 3.142

sentence = "1 MB is equal to {:,} bytes". format(1000**2)   # The result is displayed in imperial system
print(sentence)
# Output = 1 MB is equal to 1,000,000 bytes

import datetime
my_date = datetime.datetime (2016, 9, 24, 12, 30, 45)
print (my_date)
# Output = 2016-09-24 12:30:45

# Link = "https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior"
sentence = "{:%B %d, %Y}".format(my_date)        # Use the website to print it in a specific order
print(sentence)                                  # %B for month     %d for day    %Y for year
# Output = September 24, 2016

# Layout = March 01, 2016 fell on a Tuesday and was the 061 day of the year.
sentence = "{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year".format(my_date)
print (sentence)

