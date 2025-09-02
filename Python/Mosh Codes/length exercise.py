name = input("Enter your name: ")
if len(name) < 3:
    print("Name is too short")
elif len(name) > 50:
    print("Name is too long")
else:
    print(f"{name} is a good name")
