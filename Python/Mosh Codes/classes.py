class Car:
    def wheels(self):
        return "Wheels are round"

    def spoilers(self):
        return "Spoilers are present for all cars"

    class Mustang:
        def motor(self):
            return "No"

        def shape(self) :
            return "Muscle car"

    class Benz:
        def motor(self):
            return "Yes"

        def shape(self) :
            return "Sports car"

c1 = Car()
print(c1.Mustang.motor())
'''
m1 = Mustang()
m1.color = "Red"                                            # Giving the class object an attribute
print("Motor : " + m1.motor())                       # "motor" is an object in the child class so use parenthesis
print("Shape is: " + m1.shape())
print("Color required: " + m1.color + "\n")                     #color" is an attribute given to the child class Mustang

b1 = Benz()
b1.color = "Green"
print("Benz is: " + b1.motor())
print("Shape is: " + b1.shape())
print("Color required: " + b1.color) '''
