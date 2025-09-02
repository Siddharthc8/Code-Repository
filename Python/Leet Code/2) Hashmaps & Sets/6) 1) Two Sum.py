def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if target - nums[i] == nums[j]:
                return ([i, j])
    return False


def two(nums, target):

    index_dict = {}

    for i,n in enumerate(nums):
        sub_target = target - n
        if sub_target in index_dict:
            return[index_dict[sub_target], i]
        index_dict[n] = i
    return []

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))