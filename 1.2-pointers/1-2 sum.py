def twoSum(nums, target):
    numbs = list(enumerate(nums))
    numbs.sort(key=lambda x: x[1])
    left = 0
    right = len(numbs) - 1
    while target != numbs[left][1] + numbs[right][1]:
        if target > numbs[left][1] + numbs[right][1]:
            left += 1
        elif target < numbs[left][1] + numbs[right][1]:
            right -= 1
    return [numbs[left][0], numbs[right][0]]
print(twoSum([2, 11, 7, 15], 9))