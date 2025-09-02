import os
import chardet
from charset_normalizer import from_path

print(os.getcwd())
os.chdir("/Users/Siddharth1/Desktop")


with open("Companies.txt", "r") as f:
    with open("test.txt", "w") as d:
        names = [line.replace('\xa0', '').strip() for line in f if line.strip()]
        no_rep = []
        for item in names:
            if item not in no_rep:
                no_rep.append(item)
                d.write(item + "\n")
