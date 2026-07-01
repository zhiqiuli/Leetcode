'''
n = 3, k = 3, row = 0, column = 0
after  1  steps, dp= [[0, 0, 0], [0, 0, 1], [0, 1, 0]]
after  2  steps, dp= [[2, 0, 1], [0, 0, 0], [1, 0, 0]]
after  3  steps, dp= [[0, 1, 0], [1, 0, 3], [0, 3, 0]]
'''
DIR = ((1,2),(-1,-2),(1,-2),(-1,2),(2,1),(-2,-1),(2,-1),(-2,1))
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1 # 起始位置: dp[k][x][y] after k steps, how many ways to get (x, y)
        for k_ in range(k):
            dp_next = [[0] * n for _ in range(n)]
            for x in range(n):
                for y in range(n):
                    if dp[x][y] >= 1: # 只要不是0的话，就能move
                        for (dx, dy) in DIR:
                            x_next, y_next = x + dx, y + dy
                            if x_next < 0 or x_next >= n or y_next < 0 or y_next >= n:
                                continue
                            dp_next[x_next][y_next] += dp[x][y] # 累计之前的步数
            dp = [c[:] for c in dp_next]
            print('after ', k_ + 1, ' steps, dp=', dp)
        
        res = 0
        for x in range(n):
            for y in range(n):
                res += dp[x][y]
        print(res, k)
        return res / (8 ** k)
