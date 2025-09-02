class Fibonacci():
    pass

def fib(n):
    a, b, temp = 0, 1, 0

    if n <= 0:
        return False
    if n == 1:
        return 0, 1
    print(0, 1, end = " ")
    for i in range(1, n):
        temp = a + b
        a = b
        b = temp
        print(temp, end = " ")




def Fibonacci(n):
    if n == 0:
        # print("Error")
        return False
    elif n==1:
        series = [0]
        return series
    a, b = 0, 1
    series = []
    for i in range(n):
        series.append(a)
        a, b = b, a+b
    return series


# l = 2
# out = Fibonacci(2)
# print(out)



def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# # Input: Number of terms
# n = int(input("Enter the number of terms: "))
#
# # Generate and print the Fibonacci series
# if n <= 0:
#     print("Please enter a positive integer.")
# else:
#     result = [fibonacci_recursive(i) for i in range(n)]
#     print("Fibonacci series:", result)



def Fib(n):

    series = [0]
    a, b = 0, 1
    for i in range(n):
        series.append(b)
        a, b = b, a+b
    return series


# print(fib(3))



def Fin(n: int):

    a , b = 0, 1
    if n ==  0: return None
    # if n == 1: print()
    print(0, 1, end = " ")

    for i in range(1, n):
        a , b = b, a+ b
        print(b, end = " ")

# Fin(10)

def Finn(n):
    if n <= 0: return 0
    if n == 1: return 0, 1
    else : return Finn(n-1) + Finn(n-2)

# n=10
# res  = [ Finn(i) for i in range(n)]
# print(res)


print(fibonacci_recursive(3))