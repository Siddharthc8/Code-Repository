import os

f = open("test.txt", "r+")   # r = read, w = write, a = append, r+ = reading and writing
f.close()         # Closes the file
print(f.mode)     # print the mode like either reading or writing
print(f.name)     # Prints the name

# Opening file using Contacts Manager       Preferred

with open("test.txt", "r") as f:
    f_contents = f.read(10)             # Reads and stores in the placeholder
    f_first_line = f.readline()         # Reads the first line and the second line if executed again
    f_all_lines = f.readlines()         # Reads and stores all the lines in the file
    print(f_contents)
    print(f_first_line)
    print(f_all_lines)

# To iterate lines in a big file
with open("test.txt", "r") as f:
    for line in f:                      # Prints all the lines in the file
        print(line, end="")

with open("test.txt", "r") as f:
    f_contents = f.read(100)              # Prints the first 100 characters in my file
    print(f_contents)                     # and executing will start from where it last read
    f_contents = f.read(100)              # until file is full read to return an empty result
    print(f_contents)

with open("test.txt", "r") as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end= "/")
    f_contents = f.read(size_to_read)
    print(f_contents)
    print(f.tell())                   # f.tell() returns the no of characters read or the position of the ead pointer
    print(f.seek(1))                  # f.seek() sets the read pointer to that particular position in the file

while len(f_contents) > 0:
    print(f_contents, end="/")
    f_contents = f.read(size_to_read)


# Writing to files
with open("test.txt", "w") as f:           # Replaces if a file exists careful when using this command
    f.write("Old text is old")
    f.seek(0)                               # Sets the write pointer to the mentioned position
    f.write("New text")                     # Replaces whatever is the position while writing after seek

with open("test.txt", "r") as rf:
    with open("test_copy.txt", "w") as wf:
        for line in rf:
            wf.write(line)

# Reading and writing pictures                 # "rb" and "wb" can be used for text files as well
with open("test.txt", "rb") as rf:            # Use "rb" for reading and pass in .jpg format
    with open("test_copy2.txt", "wb") as wf:   # Use "wb" for writing and pass in .jpg format
        for line in rf:
            wf.write(line)

with open("test.txt", "r") as rf:
    with open("test.txt", "w") as wf:           # Opens up a new file but replaces if already present be careful
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk)>0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)


