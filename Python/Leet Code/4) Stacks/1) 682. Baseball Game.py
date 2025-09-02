def calPoints(operations: list[str]) -> int:
    stack = []
    for i in operations:
        if i == "+":
            stack.append(stack[-1] + stack[-2])
        elif i == "D":
            stack.append(stack[-1] * 2)
        elif i == "C":
            stack.pop()
        else:
            stack.append(int(i))
    return sum(stack)


def callPoints(operations: list[str]) -> int:
    stack = []
    for i in operations:
        if i.isdigit() or i.startswith("-") and i[1:].isdigit():
            stack.append(int(i))
        elif i == "+":
            stack.append(stack[-1] + stack[-2])
        elif i == "D":
            stack.append(stack[-1] * 2)
        elif i == "C":
            stack.pop()

    return sum(stack)


operations = ["5","2","C","D","+"]
ops = ["5","-2","4","C","D","9","+","+"]
ops1 = ["1","C"]

print(calPoints(operations))
print(callPoints(operations))

print(calPoints(ops))
print(callPoints(ops))

print(calPoints(ops1))
print(callPoints(ops1))