def maxArea(height):
    l = 0
    r = len(height) - 1
    m = 0
    while l < r:
        w = r - l
        h = min(height[l], height[r])
        m = max(m, w * h)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return m
print(maxArea([2, 1, 5, 3, 6, 4]))