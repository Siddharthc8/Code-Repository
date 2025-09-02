palindromes = [

    "repaper",
    "detartrated",
    "tattarrattat",
    "A man, a plan, a canal, Panama",
    "Sir, I demand, I am a maid named Iris",
    "Eva, can I see bees in a cave?",
    "Mr. Owl ate my metal worm",
    "A Santa lived as a devil at NASA"
]



def longest_pal(pals: list):
    count_list = []
    for i in range(len(pals)):
        pal = pals[i]
        pal = pal.lower()
        count = 0
        for j in range(len(pal)):
            l = len(pal)
            if pal[j] != pal[ l - 1 - j ]:
                count = 0
                break
            count += 1
        count_list.append(count)
    return count_list


# def find_max(ott: list):
#     maxim = 0
#     ind = 0
#     for i in range(len(out)):
#         if maxim < out[i]:
#             maxim = out[i]
#             ind = i
#         elif max == out[i]:
#
#
#     return ind, maxim

# out = longest_pal(palindromes)
# print(find_max(out))





def is_palindrome(s):
    s = "".join(char.lower() for char in s if char.isalnum())
    if len(s) < 2: return True
    if s[0] != s[-1] : return False
    return is_palindrome(s[1:-1])

valid_palindromes = [ p for p in palindromes if is_palindrome(p) ]
longest_palindromes = max(valid_palindromes, key = len)

print("Longest palindromes: ", longest_palindromes)






