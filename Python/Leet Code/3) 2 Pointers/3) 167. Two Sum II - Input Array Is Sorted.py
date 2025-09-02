def twosum_2(nums, target):
    n = len(nums)
    L, R = 0, n-1

    while L < R:
        sum = nums[L] + nums[R]
        if sum == target:
            return ( [L+1, R+1] )
        elif sum > target:
            R -= 1
        else:
            L += 1

numbers = [2, 7, 11, 15]
target = 9


print(twosum_2(numbers, target))