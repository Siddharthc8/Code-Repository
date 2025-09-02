import os

current_path = "/Users/Siddharth1/Documents/Disk-D/VLSI and Microelectronics/Python/Dummy"
os.chdir(current_path)  # Change cd

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)              # Splits the name and extension
    # os.remove(".DS_Store")
    # print(f_name, f_ext)
    f_title, f_course, f_num = f_name.split("-")     # Return three values as we have two dashes in the actual file name

    f_title = f_title.strip()                        # Strips all the empty spaces
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)                   # .zfill(2) fills with zeros upto 2 places before the number
    #                                                    # Also make sure it is the first character for it be executed
    new_name = "{}-{}{}".format(f_num, f_title, f_ext)

    os.rename(f, new_name)

# with open("Dummy.py", "w") as f:                                 # Open a new file
#     pass

# for i in range(3):                                             # Creating multiple files
#     open(f"Dummy_{i}.txt", "w").close()

# os.remove("Dummy.txt")
# print(os.getcwd())
# print(os.listdir())
# for f in os.listdir():
#    print(f)

# Workplace


