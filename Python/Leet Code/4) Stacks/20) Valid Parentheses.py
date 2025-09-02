def isValid(s: str) -> bool:
    stack = []
    map = {")": "(", "]": "[", "}": "{"}

    for c in s:
        if c in map:
            top_element = stack[-1] if stack else "#"
            if top_element != map[c]:
                return False
            else:
                stack.pop()
        else:
            stack.append(c)
    return not stack


# Test Case 1 - Simple valid case
print(isValid("()"))  # True

# Test Case 2 - Multiple types
print(isValid("()[]{}"))  # True

# Test Case 3 - Nested valid
print(isValid("([{}])"))  # True

# Test Case 4 - Mismatched
print(isValid("(]"))  # False

# Test Case 5 - Unclosed
print(isValid("("))  # False

# Test Case 6 - Empty string
print(isValid(""))  # True

# Test Case 7 - Wrong order
print(isValid("([)]"))  # False

# Test Case 8 - Complex valid
print(isValid("{[]}({})"))  # True

# Test Case 9 - Only closing
print(isValid("]"))  # False

# Test Case 10 - Long valid
print(isValid("((((([])))))"))  # False