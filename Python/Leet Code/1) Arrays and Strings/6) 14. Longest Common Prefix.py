# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
# Constraints:
# * 1 <= strs.length <= 200
# * 0 <= strs[i].length <= 200
# * strs[i] consists of only lowercase English letters if it is non-empty.

strs = ["flower","flow","flight"]

def commonPrefix(strgs):
    if not strgs:
        return ""
    prefix = strgs[0]                       # The common prefix of any word can be a max of the same word
    for word in strgs:
        while not word.startswith(prefix):  # Using startswith()
            prefix = prefix[:-1]            # Decreasing prefix for everytime it becomes false
            if not prefix:
                return ""
    return prefix



def neet(strgs):

    res = ""
    prefix = strgs[0] # ----------------------------------------------------------------------
    for i in range(len(prefix)):                                                    #         |
        for s in strgs:                                                             #         |
            if len(s) == i or s[i] != strgs[0][i]:  # len(s) is compared with i because the prefix is used to iterate i
                return res
        res += s[i]
    return res



def greg(strgs):

    min_length = float("inf")

    for s in strgs:
        if len(s) < min_length:
            min_length = len(s)

    i = 0
    while i < min_length:
        for s in strgs:
            if s[i] != strgs[0][i]:
                return s[:i]

    return s[:i]         # Incase of empty string


neet(strs)
print(commonPrefix(strs))