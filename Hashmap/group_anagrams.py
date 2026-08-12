class Solution(object):
    def groupAnagrams(self, strs):
        hashset={}
        for i,word in enumerate(strs):
            a="".join(sorted(word))
            if a not in hashset:
                hashset[a]=[word]
            else:
                hashset[a].append(word)
        return list(hashset.values())

ans=Solution()
print(ans.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))