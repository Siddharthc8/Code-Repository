def threesum(nums):
    map = {}
    res = set()
    n = len(nums)

    for i, num in enumerate(nums):
        map[num] = i

    for i in range(n):
        for j in range(i+1, n):
            desired = -(nums[i] + nums[j])
            if desired in map and map[desired] != i and map[desired] != j:
                res.add(tuple(sorted([desired, nums[i], nums[j]])))

    return res


nums = [-1,0,1,2,-1,-4]

print(threesum(nums))