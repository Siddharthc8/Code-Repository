# Given an integer array `nums` sorted in **non-decreasing order**, remove some duplicates **in-place** such that each unique element appears **at most twice**. The relative order of the elements should be kept the **same**.
#
# Since it is impossible to change the length of the array in some languages, you must instead have the result placed in the first part of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.
#
# Return `k` after placing the final result in the first `k` slots of `nums`.
#
# **Do not allocate extra space for another array.** You must do this by modifying the input array **in-place** with **O(1) extra memory**.
#
# ---
#
# **Custom Judge:**
# The judge will test your solution with the following code:
# ```java
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
#
# int k = removeDuplicates(nums); // Calls your implementation
#
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# ```
# If all assertions pass, then your solution will be **accepted**.
#
# ---
#
# **Example 1:**
# ```
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2, and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# ```
#
# **Example 2:**
# ```
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3, and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# ```
#
# ---
#
# **Constraints:**
# - `1 <= nums.length <= 3 * 10^4`
# - `-10^4 <= nums[i] <= 10^4`
# - `nums` is sorted in **non-decreasing order**.


# This is checking one step back and probably easy to come up with the logic
def remove(nums):
    j = 1
    count = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            count += 1
        else:
            count = 1
        if count <= 2:
            nums[j] = nums[i]
            j += 1
    print(nums)
    return j


#  Think of j as write pointer and i as the read pinter.
# NOTE: For this method " for i in nums:" can be used as well
def remove_two_pointers(nums):
    if len(nums) <= 2:
        return 2
    j = 2
    for i in range(2, len(nums)): # "for i in nums:" can also be used
        if nums[i] != nums[j-2]:
            nums[j] = nums[i]
            j+=1
    print(nums)
    return j


nums = [1,1,1,2,2,3]
nums1 = [0,0,1,1,1,1,2,3,3]

print(remove(nums))
print(remove(nums1))

print(remove_two_pointers(nums))
print(remove_two_pointers(nums1))