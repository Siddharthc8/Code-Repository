def zigzag(s, numRows):
    res = [[] for _ in range(numRows)]    # Make sure to use range
    i = 0
    d = 0
    for c in s:
        res[i].append(c)
        if i == 0:
            d = 1
        elif i == numRows -1:
            d = -1
        i += d
    ans = ""
    for i in range(numRows):
        ans += "".join(res[i])
    return (ans)

def myown(s: str, numRows: int) -> str:

    ans = [[] for _ in range(numRows)]   # range here is important
    up, down = 1, 0
    direction = up
    i, j = 0, 0

    for c in s:

        ans[j] += c # or ans[j].append(c)

        if direction == up:
            if j < numRows-1:
                j += 1
            elif j == numRows-1:
                direction = down
                j -= 1

        elif direction == down:
            if j > 0:
                j -= 1
            elif j == 0:
                direction = up
                j += 1
    res = ""
    for i in range(numRows):
        res += "".join(ans[i])

    return res

print(zigzag(s = "PAYPALISHIRING", numRows = 3))
print(zigzag(s = "A", numRows = 1))