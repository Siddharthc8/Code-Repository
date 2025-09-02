class Girl:

    gender = "female"         # Common for the class like default for the class

    def __init__(self, name):
        self.name = name


r = Girl("Rachel")
s = Girl("Stanky")
print(r.gender)
print(r.name)
print(s.gender)
print(s.name)
