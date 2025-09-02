import os                                           # Opening is not reading
from datetime import datetime

print(os.__file__)                                  # To print the directory of the library
print(dir(os))                                      # Lists all the attributes and methods

print(os.getcwd())

# Change Directory
os.chdir("/Users/Siddharth1/Documents/Disk-D/VLSI and Microelectronics/Python/Corey_Python")

print(os.listdir())                             # To list all the items in the directory

# Create new directories or folders
os.mkdir('OS-Demo-2')                           # Only one argument or can only create that particular folder
os.makedirs('OS-Demo-2/ Sub_directory')         # Can also create sub folders taking the paths as arguments

# Removing or deleting directories
os.rmdir('OS-Demo-2')                           # Only one argument or can only create that particular folder
os.removedirs('OS-Demo-2/ Sub_directory')       # Removes the whole path so careful before using it

os.rename("old_name.txt", "new_name.txt")        # Old_name first and new_name next

# To print all the info about a file
f = open("new_name.txt", "r ")
f = open("new_file.txt", "w")
f.write("TO SEE THE SIZE OF THE FILE")
print(os.stat("new_file.txt"))                      # Will list all the info about the file
print(os.stat("new_file.txt").st_size)              # Will print the size of the text

mod_time = os.stat("new_file.txt").st_mtime
print(datetime.fromtimestamp(mod_time))            # To display in human-readable format

for dir, sub_dir, file_names in os.walk(os.getcwd()):     # Returns three values so three items in for loop
    print("Current directory:", dir)
    print("Sub Directories:", sub_dir)
    print("Files:", file_names)

print(os.environ.get("HOME"))                         # environ.get("HOME") Prints the home directory

file_path = os.path.join(os.environ.get("HOME"), "test.txt")      # To join/concatenate two paths
print(file_path)

print(os.path.basename("/tmp/test.txt"))                # To print the basename of the path ie the file name with ext
print(os.path.dirname("/tmp/test.txt"))                 # To print the directory name
print(os.path.split("/tmp/test.txt"))                   # To print both the whole path and, the file name as a tuple

print(os.path.exists("/tmp/test.txt"))                # To check if a path exists returns True or False
print(os.path.isdir("/tmp/test.txt"))                 # To check if it is a directory or not, returns True or False
print(os.path.isfile("/tmp/test.txt"))                # To check if it is an existing file or not, returns True or False

print(os.path.splitext("/tmp/test.txt"))              # Splits the file extension as a separate entity as a tuple

with open(file_path, "w") as f:
    f.write("Hello")

f  = open("new_file.txt", "w")                      # Mention the action
f.write("This is a new file you dummy")
f.close()                                           # To close a file

f.write("\nThis is a just additional text")         # Write some text to a file
f = open("new_file.txt")
print(f.read())

os.remove("filename.txt")                     # Remove an existing file


