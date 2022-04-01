class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        
        n, m = len(mat), len(mat[0])
        
        N = min(n, m)
        minSizeList = [0] * (N + 1)

        # calculate the prefix sum
        prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prefix_sum[i][j] =  prefix_sum[i-1][j  ] \
                                  + prefix_sum[i  ][j-1] \
                                  - prefix_sum[i-1][j-1] \
                                  + mat       [i-1][j-1]
        
        print(prefix_sum)
        
        # x2,y2小于x1,y1 计算时记得-1
        range_sum = lambda dp, x1, y1, x2, y2 : \
                           dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
        
        ans = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # for k in range(N):
                for k in range(ans, N): # 优化 记住此时k的循环在i，j之内
                    # 计算超出的范围
                    if i + k > n or j + k > m:
                        break
                    if range_sum(prefix_sum, i, j, i + k, j + k) > threshold:
                        break
                    ans = max(ans, k + 1)
        return ans
