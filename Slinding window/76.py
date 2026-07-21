from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""
        need = Counter(t)
        window = {}
        have = 0
        need_count = len(need)
        l = 0
        res = [-1, -1]
        res_len = float("inf")
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                have += 1
            while have == need_count:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
ans=Solution()

print(ans.minWindow("ADOBECODEBANC", "ABC"))