counter=0
numbers=[1,1,2,1,1,1,1,1,9,1,2,3,4,4,4,4,4,4,4,4,4,5,6,7,8,9,9]
num_del=int(input("enter a number to be deleted: "))
for number in numbers:
    if number == num_del:
        counter +=1
print(numbers)
for x in range(counter-1):
    numbers.remove(num_del)
print(numbers)