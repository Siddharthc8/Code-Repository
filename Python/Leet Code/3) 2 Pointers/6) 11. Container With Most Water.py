def maxArea(height):
    n = len(height)
    R = n - 1
    L = 0
    max_area = 0
    while L < R:
        h = min(height[L], height[R])
        w = R - L
        area = w * h
        max_area = max(max_area, area)

        if height[L] > height[R]:
            R -= 1
        else:
            L += 1
    return max_area
