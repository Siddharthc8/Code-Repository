def prod(nums):
    res = [1] * len(nums)
    pre = 1
    post = 1
    n = len(nums)
    for i in range(0, len(nums)):
        res[i] = res[i] * pre   # Multiplication because when i reaches 3 where post has already been calculated pre shouldn't replace it
        pre = pre * nums[i]

        res[n -1 -i] *= post
        post = post * nums[n -1 -i]
    return (res)


nums = [1,2,3,4]
nums1 = [-1,1,0,-3,3]

print(prod(nums))
# print(prod(nums1))


def single_loop(nums):
    n = len(nums)
    res = [1] * n

    # Initialize prefix and suffix products
    prefix = 1
    suffix = 1

    for i in range(n):
        # Update the result with the prefix product
        res[i] *= prefix
        prefix *= nums[i]

        # Update the result with the suffix product
        res[n - 1 - i] *= suffix
        suffix *= nums[n - 1 - i]

    return res