from pathlib import Path

# Absolute path
# c: \Program Files\Microsoft
# /usr/local/bin

# Relative path

path = Path(/Users/Siddharth1/Documents/Disk-D/VLSI and Microelectronics)
for file in path.glob("*.c"):
        print(file)

