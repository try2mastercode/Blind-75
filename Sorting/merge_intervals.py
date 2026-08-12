"""LeetCode 56 - Merge Intervals.
Given a list of intervals, merge all overlapping intervals and return the result.
Example: [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]
"""
class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        result = []
        while len(intervals) != 0:
            if len(result) == 0 or result[-1][1] < intervals[0][0]:
                result.append(intervals.pop(0))
            elif result[-1][1] >= intervals[0][0] and result[-1][1] <= intervals[0][1]:
                result[-1][1] = intervals[0][1]
                intervals.pop(0)
            elif result[-1][1] >= intervals[0][0] and result[-1][1] > intervals[0][1]:
                intervals.pop(0)
        return result
ans=Solution()
print(ans.merge([[4,7],[1,4]]))