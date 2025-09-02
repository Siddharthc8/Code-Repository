numbers=[1,1,2,1,1,1,1,1,9,1,2,3,4,4,4,4,4,4,4,4,4,5,6,7,8,9,9]
num_del = int(input("Enter a number to be deleted: "))
count = 0
numbers.reverse()

for n in numbers:
    if n == num_del:
        count += 1

for i in range(0, count-1):
    numbers.remove(num_del)

numbers.reverse()

print(numbers)
