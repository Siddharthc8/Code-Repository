def is_palindrome(strg):
    for i in range(0, len(strg)//2):
        if strg.lower() != strg[::-1].lower():
            print(strg.lower())
            return False
        return True

strg = "Malayalam"
print(is_palindrome(strg))


def palindrome(strg):
    length = len(strg)
    strg = strg.lower()
    for i in range(0,len(strg)//2):
        if strg[i] != strg[len(strg) -1 -i]:
            return False
        return True

strg = "Malayalam"
print(palindrome(strg))

# Recursive functions

def pal_rec(word):
    word = word.lower()
    if len(word) < 2: return True          # Checks if it is one letter
    if word[0] != word[-1]: return False   # Normal palindrome check first and last letter
    return pal_rec(word[1:-1])             # Here we slice the checked char and send the rest to the function again

def pal_short(s):
    return len(s) < 2 or s[0] == s[-1] and pal_short(s[1:-1])     # Mentioning all the cases for true

#///////////////////////////////////////////////////////////////////////////////////////////
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

def is_palindrome(s):
    s = "".join(char.lower() for char in s if char.isalnum())
    if len(s) < 2: return True
    if s[0] != s[-1] : return False
    return is_palindrome(s[1:-1])

valid_palindromes = [ p for p in palindromes if is_palindrome(p) ]
longest_palindromes = max(valid_palindromes, key = len)

print("Longest palindromes: ", longest_palindromes)

