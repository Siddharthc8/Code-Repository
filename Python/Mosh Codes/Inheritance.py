'''class Dog:
    def walk(self):
        print("I am walking")

class Cat:
    def walk(self):
        print("I am walking")'''


# The above code is repeating itself so use inheritance

class Mammal:
    def walk(self):
        print("I am walking")


class Dog(Mammal):
    def __init__(self,name):
        self.name = name

    def sound(self):
        print("Bark")


class Cat(Mammal):
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Meow")


snoopy = Dog("Snoopy")
snoopy.sound()

tomcat = Cat("Tomcat")
tomcat.sound()