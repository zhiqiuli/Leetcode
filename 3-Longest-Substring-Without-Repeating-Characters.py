class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        # 经典双指针问题
        last_seen = {}
        left = 0
        longest = 0

        for right, char in enumerate(s):
            if char in last_seen: # 先检查char是否已经存在在扫描过的数组中
                left = max(left, last_seen[char] + 1) # 如果存在的话，使用lastseen右+1的位置作为substring开始
            
            last_seen[char] = right # 无论如何都需要更新lastSeen
            longest = max(longest, right - left + 1) # 无论如何都更新答案

        return longest