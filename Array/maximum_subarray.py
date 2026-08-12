"""LeetCode 53 - Maximum Subarray (Kadane's algorithm).
Given an array of integers, find the maximum sum of any contiguous subarray.
"""
class Solution(object):
    def maxSubArray(self, nums):
        curr_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum
ans=Solution()
print(ans.maxSubArray([-2,1,-3,4,-1,2,1,-2,4]))
