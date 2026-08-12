class Solution(object):
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        result=[]
        while len(intervals)!=0:
            if len(result)==0 or result[-1][1]<intervals[0][0]:
                result.append(intervals.pop(0))
            elif result[-1][1]>=intervals[0][0] and result[-1][1]<=intervals[0][1]:
                result[-1][1]=intervals[0][1]
                intervals.pop(0)
            elif result[-1][1]>=intervals[0][0] and result[-1][1]>intervals[0][1]:
                intervals.pop(0)
        return result

ans=Solution()
print(ans.insert([[4,7],[1,4]],[2,4]))