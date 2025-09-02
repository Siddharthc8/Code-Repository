def climbStairs(n: int):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    two_back = 1
    one_back = 2
    for i in range(2, n):
        next_num = two_back + one_back
        print("next_num =", next_num)
        two_back = one_back
        print("two_back =", two_back)
        one_back = next_num
        print("one_back =", one_back)
        print(one_back)
    return one_back

print(climbStairs(5))