i = 0
while i < 3:
    num = int(input("Guess: "))
    if num == 8:
        print("You got it asshole!")
        break
    i += 1

else:
    print("Sorry you failed!")
