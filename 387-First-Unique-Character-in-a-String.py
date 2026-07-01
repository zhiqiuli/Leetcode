from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        unique = set()
        for key, val in c.items():
            if val == 1:
                unique.add(key)
        for i in range(len(s)):
            if s[i] in unique:
                return i
        return -1