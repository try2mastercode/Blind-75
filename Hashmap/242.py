class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        def get_frequency(s):
            hashset = {}
            for i in s:
                if i not in hashset:
                    hashset[i] = 1
                else:
                    hashset[i] += 1
            return hashset

        hashset1 = get_frequency(s)
        hashset2 = get_frequency(t)
        if sorted(list(hashset1.keys())) != sorted(list(hashset2.keys())):
            return False
        for i in hashset1:
            if hashset1[i] != hashset2[i]:
                return False
        return True
ans=Solution()
print(ans.isAnagram("nagaram","anagram"))