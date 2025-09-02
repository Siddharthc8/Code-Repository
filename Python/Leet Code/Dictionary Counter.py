from collections import Counter

n = [1,1,4,2,3,3,4]

def is_possible_to_split(nums):
    counter = Counter(nums)

    for f in counter.values():
        if f > 2:
            return False
    return True

# print(is_possible_to_split(n))

def isPossibleToSplit(nums):
    counter = {}

    for n in nums:

        if n in counter.keys():
            counter[n] += 1
        else:
            counter[n] = 1

    print(counter)

    for f in counter.values():
        if f > 2:
            return False
    return True

# print(isPossibleToSplit(n))


def isPossibleToSplit2(nums):
    counter = {}

    for n in nums:
        counter[n] = counter.get(n, 0) + 1
    print(counter)

    for f in counter.values():
        if f > 2:
            return False
    return True

print(isPossibleToSplit2(n))

