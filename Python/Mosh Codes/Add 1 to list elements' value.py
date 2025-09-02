# Consider the whole list to be a single number and add 1 to it

digits = ["9", "9", "9", "9"]
int_of_digits = int("".join(map(str, digits))) + 1
digits.clear()
for item in str(int_of_digits):
    digits.append(int(item))

print(digits)