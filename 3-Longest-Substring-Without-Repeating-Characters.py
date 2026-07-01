class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        index = {}
        i = 0
        index[s[i]] = i
        res = 1
        for j in range(1, len(s)):
            if s[j] in index:
                i = max(i, index[s[j]] + 1) # remember that i only moves to the right, so the max is needed!
            index[s[j]] = j
            res = max(res, j - i + 1)
        return res