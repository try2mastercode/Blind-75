a="pwwkew"


def lengthOfLongestSubstring(s):
    if len(s) == 1 or len(set(s))==1:
        return 1
    if len(s) == 0:
        return 0
    m = 0
    i, j = 0, 2
    while i <= len(s) - 1 and j <= len(s) - 1:
        if len(set(s[i:j])) == len(s[i:j]):
            m = max(m, len(s[i:j]))
            print(s[i:j])
            j = j + 1
        else:
            i = j-1

    return m
print(lengthOfLongestSubstring("aa"))