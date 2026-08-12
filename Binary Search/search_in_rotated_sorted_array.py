class Solution(object):
    def search(self, nums, target):
        if target not in nums:
            return -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
ans=Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(ans.search(nums, target))