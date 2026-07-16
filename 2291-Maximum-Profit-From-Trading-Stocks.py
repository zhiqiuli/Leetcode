class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        dp = [0] * (budget + 1)
        for present_px, future_px in zip(present, future):
            profit = future_px - present_px
            
            if profit <= 0 or present_px > budget:
                continue
            
            # from budget decreasing to present px (inclusive)
            for money in range(budget, present_px - 1, -1):
                dp[money] = max(
                    dp[money], # skip
                    dp[money - present_px] + profit # buy
                    )
            
            # print([i for i in range(budget + 1)])
            # print(dp)
            # print('---')

        return dp[-1]