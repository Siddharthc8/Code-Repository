

def two_pointer(s):
    n = len(s)
    L , R  = 0, n-1

    while L < R:
        s[L], s[R] = s[R], s[L]
        L += 1
        R -= 1


def reverse(s):
    n = len(s)
    for i in range(n//2):
        s[i], s[n-1 - i] = s[n-1 - i], s[i]


# Test Case 1 - Odd length
s = ["h","e","l","l","o"]
two_pointer(s)
print(s)  # ["o","l","l","e","h"]

# Test Case 2 - Even length
s = ["H","a","n","n","a","h"]
two_pointer(s)
print(s)  # ["h","a","n","n","a","H"]

# Test Case 3 - Single character
s = ["A"]
two_pointer(s)
print(s)  # ["A"]