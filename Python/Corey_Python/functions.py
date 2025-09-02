# def hello_func(greeting, name = "You"):                  # Prints the default value for kwargs in this case where kwargs argument is not passed
#     return (f"{greeting} {name}")
#
# print(hello_func("Hello"))
# print(hello_func("Hello", name = "Jane"))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

# student_info("Math", "Art", name = "John", age = 32)       # Creates a dictionary for "name" and "age"

courses = ["Math", "Art"]
info = {'name': 'John', 'age': 32}

# student_info(courses, info)                 # Passes both courses and info to args
student_info( *courses, **info)

