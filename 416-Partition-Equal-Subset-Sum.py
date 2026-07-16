class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) // 2
        
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for n in range(target, num - 1, -1):
                dp[n] = dp[n] or dp[n - num]
        
        return dp[-1]