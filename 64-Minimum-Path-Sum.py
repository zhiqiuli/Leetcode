class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        
        for i in range(1, len(dp)):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        
        for j in range(1, len(dp[0])):
            dp[0][j] = grid[0][j] + dp[0][j-1]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]