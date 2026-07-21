class Solution(object):
    def findMin(self, nums):
        l = 0
        r = len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]
ans=Solution()
nums = [3,4,5,1,2]
print(ans.findMin(nums))