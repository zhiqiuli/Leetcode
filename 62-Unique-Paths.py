class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        numPath = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            numPath[i][0] = 1
        
        for j in range(n):
            numPath[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                numPath[i][j] = numPath[i-1][j] + numPath[i][j-1]
        
        return numPath[-1][-1]