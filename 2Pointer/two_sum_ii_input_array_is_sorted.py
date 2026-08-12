def twoSum(numbers, target):
    num = list(enumerate(numbers, start=1))
    l = 0
    r = len(numbers) - 1
    while target != num[l][1] + num[r][1]:
        if target > num[l][1] + num[r][1]:
            l += 1
        elif target < num[l][1] + num[r][1]:
            r -= 1
    return [num[l][0], num[r][0]]
print(twoSum([2, 11, 7, 15], 9))