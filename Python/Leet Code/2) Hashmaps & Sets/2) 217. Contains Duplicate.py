def duplicate(nums):
    res = {}
    for n in nums:
        if n not in res:
            res[n] = 1
        else:
            return True
    return False



def sets(nums):
    i = len(nums)
    j = len(set(nums))
    if i != j:
        return True
    return False