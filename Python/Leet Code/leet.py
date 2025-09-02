# class Solution:
#
#     def plusOne(self, digits: list[int]) -> list[int]:
#
#         string = ""
#         for i in digits:
#             string += str(i)
#
#         string = int(string) + 1
#
#         res = []
#         for i in str(string):
#             res.append(int(i))
#
#         return res
#
#
# digits = [1,2,3]
# s1 = Solution()
# print(s1.plusOne(digits))

##################################################################################################################

# class Solution:
#     def plusOne(self, digits: list[int]) -> list[int]:
#
#         for i in range(len(digits) - 1, -1, -1):
#
#             if digits[i] + 1 != 10:
#                 digits[i] += 1
#                 return digits
#
#             digits[i] = 0
#
#             if i == 0:
#                 return [1] + digits
#
#
# digits = [1,2,3]
# s1 = Solution()
# print(s1.plusOne(digits))

####################################################################################################################

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         x = str(x)
#         for i in range(0, len(x)//2):
#             if(x[i] != x[len(x)-1-i]):
#                 return False
#             return True
#
# x = 121
# s1 = Solution()
# print(s1.isPalindrome(x))

####################################################################################################################

# class Solution:
#     def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#
#         nums1[m:] = nums2[0:n]
#         nums1.sort()
#         print(nums1)
#
#
# # nums1 = [1,2,3,0,0,0]
# # nums2 = [2,5,6]
# s1 = Solution()
# s1.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)

####################################################################################################################

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         m, n, i = m - 1, n - 1, m + n - 1
#         while n >= 0:
#             if m >= 0 and nums1[m] > nums2[n]:
#                 nums1[i] = nums1[m]
#                 m -= 1
#             else:
#                 nums1[i] = nums2[n]
#                 n -= 1
#             i -= 1

####################################################################################################################

# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         res = []
#         k=0
#         for n in nums:
#             if n not in res:
#                 res.append(n)
#             else:
#                 k = k+1
#
#                 # print(res)
#         nums = res
#         print(nums)
#         print(k)
#
#
# s1 = Solution()
# n1 = [0,0,1,1,1,2,2,3,3,4]
# s1.removeDuplicates(n1)

####################################################################################################################

# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         res = set(nums)
#         nums.clear()
#         for i in res:
#             nums.append(i)
#
#         print(nums)
#
#
# s1 = Solution()
# n1 = [0,0,1,1,1,2,2,3,3,4]
# s1.removeDuplicates(n1)

####################################################################################################################

# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         for i in range(2, len(nums)):
#             if(nums[i] == nums[i-1] and nums[i-2]):
#                 nums.remove(nums[])

####################################################################################################################

# nums  = [2,2,1,1,1,2,2]
# count = 0
# candidate = 0
#
# for num in nums:
#     if count == 0:
#         candidate = num
#
#     if num == candidate:
#         count += 1
#     else:
#         count -= 1
#
# print(nums.count(candidate))

####################################################################################################################

# nums = [-1,-100,3,99]
# k=3
# k%=len(nums)
# nums = (nums[-k:]) + nums[:-k]
# print(nums)

####################################################################################################################

prices = [7,1,5,3,6,4,2,11]
# prices = [7,6,4,3,1]
buy_price = prices[0]
profit = 0
sell_price = 0
if len(prices)==1:
    print(prices)
else:
    for i in prices[1:]:
        if buy_price > i:
            buy_price = i
            # print(prices.index(i))
        if profit < i-buy_price:
           profit = i-buy_price
           sell_price = i
    if sell_price>0:
        indices = prices.index(buy_price), prices.index(sell_price)
        print("indices =", indices, " profit =", profit)
        print([buy_price, sell_price])
    else:
        print("Not a good time to buy stocks")

