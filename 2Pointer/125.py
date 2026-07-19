class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left].isalnum() is False:
                left += 1
            elif s[right].isalnum() is False:
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
ans=Solution()
print(ans.isPalindrome("A man, a plan, a canal: Panama"))

