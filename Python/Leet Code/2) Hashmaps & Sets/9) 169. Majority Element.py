from collections import Counter

def majority(nums):
    count = Counter(nums)
    l = len(nums)
    for k,v in count.items():
        if count[k] > l//2:
            return k



def majorityElement(nums: list[int]) -> int:
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


def good_idea(nums):
    counter = 0
    candidate = None
    for num in nums:
        if counter == 0:
            candidate = num
        counter += (1 if num == candidate else -1)

    return candidate

def sort_method(nums: list[int]) -> int:
    nums.sort()
    n = len(nums)
    return nums[n // 2]





nums = [2,2,1,1,1,2,2]
print(majority(nums))