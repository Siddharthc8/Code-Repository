# Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order **red, white, and blue**.
#
# We will use the integers `0`, `1`, and `2` to represent the color **red**, **white**, and **blue**, respectively.
#
# You must solve this problem **without using the library's sort function**.
#
# ---
#
# **Example 1:**
# ```
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# ```
#
# **Example 2:**
# ```
# Input: nums = [2,0,1]
# Output: [0,1,2]
# ```
#
# ---
#
# **Constraints:**
# - `n == nums.length`
# - `1 <= n <= 300`
# - `nums[i]` is either `0`, `1`, or `2`.
#
# ---
#
# **Follow up:** Could you come up with a **one-pass algorithm** using only **constant extra space**?

#########################################################################################

# We can use Bucket Sort ir Quick Sort
# Quick Sort
# NOTE : While using quick sort increment i only when swapping with L and not R

def sort_quick(nums):
    L = 0
    R = len(nums) - 1
    i = 0
    def swap(a, b):
        nums[a], nums[b] = nums[b], nums[a]
    while i <= R:           # It has to be <= because the R-- would have moved the pointer but that location is still not checked for
        if nums[i] == 0:
            swap(i, L)
            L += 1
        elif nums[i] == 2:
            swap(i, R)
            R -= 1
            i -= 1
        i += 1   # Outside if else for condition matching "1