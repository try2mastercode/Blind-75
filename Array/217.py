class Solution():
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
a=Solution()
print(a.containsDuplicate([1,2,3,4,5,1]))