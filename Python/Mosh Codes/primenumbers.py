# Python program to display all the prime numbers within an interval
# def prime(number):
#
#     prime_list = []
#     for num in range(number+1):
#         if num > 1:
#             for i in range(2, num):
#                 if (num % i) == 0:
#                     break
#             else:
#                 prime_list.append(num)
#     return prime_list
#
#
# print(prime(100))



def isprime(number):
    prime_list = []
    for num in range(2, number+1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime_list.append(num)
    return prime_list

print(isprime(100))











































