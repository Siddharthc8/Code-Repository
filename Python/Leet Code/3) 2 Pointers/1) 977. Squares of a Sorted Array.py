
def sortedSquares(nums):
    n = len(nums)
    L = 0
    R = n-1
    res = [0] * n
    for i in range(n-1,-1,-1):
        if abs(nums[L]) > abs(nums[R]):
            res[i] = nums[L] ** 2
            L += 1
        else:
            res[i] = nums[R] ** 2
            R -= 1

    print(res)


nums = [-4,-1,0,3,10]
sortedSquares((nums))