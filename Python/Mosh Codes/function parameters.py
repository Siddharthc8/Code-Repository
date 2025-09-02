def greet_user(name, lastname):
    print(f"Hi {name} {lastname}! \nWelcome aboard!\n")


def calc_cost(total, shipping, discount_percent):
    total = total - total*discount_percent + shipping
    return total

print("Start")
greet_user("John", "Doe")
greet_user(lastname="Mary", name="Frampton")

#calc_cost(50, shipping=5, discount_percent=0.05)    Use this if print command is in the function
print(calc_cost(50, shipping=5, discount_percent=0.05))
#Use Positional arguments first and
