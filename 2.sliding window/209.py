'''def minSubArrayLen(target, nums):
    i, j = 0, 1
    l = len(nums)
    if sum(nums) < target:
        return 0
    while i <= len(nums) - 1 and j <= len(nums):
        if sum(nums[i:j]) < target:
            j = j + 1
        elif sum(nums[i:j]) >= target:
            # if sum(nums[i:j])==target:
            print(nums[i:j])
            l = min(l, j - i)
            i = i + 1
    return l
minSubArrayLen(6,[10,2,3])'''


def minSubArrayLen(target, nums):
    sum_ = sum(nums)
    l = len(nums)
    if sum_ < target:
        return 0
    elif sum_ == target:
        return l
    i = 0
    j = 1
    sum_ = nums[0] + nums[1]
    while i < len(nums) - 1:
        if sum_ < target:
            j += 1
            sum_ = sum_ + nums[j-1]
        elif sum_ >= target:
            l = min(l, j - i)
            sum_=sum_-nums[i]
            i += 1
            j = i + 1
    return l
print(minSubArrayLen(11,[1,2,3,4,5]))