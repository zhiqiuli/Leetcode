Method 1


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)

        # dp[i][0] := max len ends w/ nums[i] has 0 zeros (all 1's)
        # dp[i][1] := max len ends w/ nums[i] has 1 zero
        dp = [[0, 0] for _ in range(n)]
        
        dp[0][0] = nums[0]
        dp[0][1] = 1 if nums[0] == 0 else 0 # 这个不需要也行
                        
        for i in range(1, n):
            if nums[i] == 1:
                dp[i][0] = dp[i-1][0] + 1 # 011...1+1
                dp[i][1] = dp[i-1][1] + 1 # 011...0...1+1
            else:
                dp[i][0] = 0              # 01...1+0
                dp[i][1] = dp[i-1][0] + 1 # 01...1+0
        
        res = []
        for dp_ in dp:
            res.extend(dp_)
        
        return max(res) - 1


Method 2


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        res = ans = 0
        # 右指针不断的移动
        for r in range(n):
            res += nums[r]
            # [0,1,1,0] 此时l=0, r=3, res=2, 所以r-l=3>res=2，开始移动l
            while l < r and r - l > res:
                res -= nums[l]
                l += 1
            ans = max(ans, r - l) # r-l+1 如果题目要求是replace
        return ans
