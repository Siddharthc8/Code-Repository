class Solution:

    def longestConsecutive(self, nums: list[int]):
        if nums == []: return 0
        nums = list(set(nums))
        nums.sort()
        count = 1
        longest = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                count += 1
                longest = max(longest, count)
            else: count = 1

        return longest


# Better way

class Solutions:

    def longestConsecutive(self, nums: list[int]):
        s = set(nums)
        longest = 0

        for num in s:
            # print(num)
            if num - 1 not in s:
                count = 1
                while num + 1 in s:
                    count += 1
                    num += 1
                longest = max(longest, count)
        return longest

nums = [100,4,200,1,3,2]
nums2 = [0,3,7,2,5,8,4,6,0,1]
s1 = Solutions()

print("the ans =",s1.longestConsecutive(nums))
print("the ans =",s1.longestConsecutive(nums2))



print(set(nums2))