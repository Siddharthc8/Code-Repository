def threeSumClosest(nums, target):

    map = dict()
    res = set()
    n = len(nums) - 1
    min_out = float("inf")

    for i, k in enumerate(nums):
        map[k] = i

    for i in range(n):
        for j in range(i+1, n):
            for k in range(i+2):
                min_out = min(nums[i] + nums[j] + nums[k])
    return min_out




