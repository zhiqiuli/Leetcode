class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        dp = [0] * (len(s) + 1)
        dp[0] = dp[1] = 1
        for i in range(2, len(s) + 1):
            # (1) s[i-2]s[i-1] & s[i-1] are both valid
            if 10 <= int(s[i-2] + s[i-1]) <= 26 and s[i-1] != '0':
                dp[i] = dp[i-1] + dp[i-2]
            # (2) s[i-2]s[i-1] is valid & s[i-1] is not valid, such as 10 and 20
            elif s[i-2] + s[i-1] in ('10', '20'):
                dp[i] = dp[i-2]
            # (3) s[i-2]s[i-1] is not valid & s[i-1] is valid
            elif s[i-1] != '0':
                dp[i] = dp[i-1]
            # (4) neither s[i-2]s[i-1] or s[i-1] is valid 
            else:
                return 0
        return dp[-1]