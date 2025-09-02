def reducing(number):

    number = str(number)
    list = []

    for i in range(len(number)-1):
        if number[i] > number[i+1]:
            list.append(number[i])
        elif number[i] <= number[i+1]:
            list.clear()

    if number[-2] > number[-1]:
        list.append(number[-1])
    elif number[-2] <= number[-1]:
        list.clear()
        list.append(number[-1])


    return list


print(reducing(123987547362))
print(reducing(987654))
print(reducing(123456))
print(reducing(321754))