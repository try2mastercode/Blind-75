class Solution(object):
    def isValid(self, s):
        dic = {'}': '{', ')': '(', ']': '['}
        stack = []
        for i in s:
            if i == '{' or i == '(' or i == '[':
                stack.append(i)
            else:
                if stack and stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
ans=Solution()
print(ans.isValid("()"))