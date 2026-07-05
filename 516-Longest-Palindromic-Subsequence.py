class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[-1] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        
        for k in range(1, len(s)):
            for i in range(len(s) - k):
                j = i + k
                if s[i] == s[j] and k == 1: 
                    dp[i][j] = dp[i][j-1] + 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]