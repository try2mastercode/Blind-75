class Solution(object):
    def maxArea(self, height):
        l=0
        r=len(height)-1
        m=0
        while l<r:
            w=r-l
            h=min(height[l],height[r])
            m=max(m,w*h)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return m
ans=Solution()
print(ans.maxArea([1,0,1,2,3,4,5,6,7]))