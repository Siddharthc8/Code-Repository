def valid(s):

    s = "".join(c for c in s if c.isalnum()).lower()

    for i in range(len(s)//2):
        if s[i] != s[ len(s)-1 - i]:
            return False
    return True

def recursive(s):
    s = "".join(c for c in s if c.isalnum()).lower()

    return len(s) < 2 or s[0] == s[-1] and recursive(s[1:-1])

s = "A man, a plan, a canal: Panama"
print(valid(s))
print(recursive(s))