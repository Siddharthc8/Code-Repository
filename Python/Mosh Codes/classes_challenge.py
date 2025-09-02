class Person:                     # Also called as Type
    def __init__(self, name):     #Constructor
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")

P1 = Person("John Smith")      # P1 is an object of the class
P1.talk()

P2 = Person("Bob Smith")       # P2 is another object of the class
P2.talk()
