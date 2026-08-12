class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1
ans=Solution()
nums = [-1,0,3,5,9,12]
target = 9
print(ans.search(nums, target))