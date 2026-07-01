DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        num_of_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.dfs(i, j, grid, visited)
                    num_of_islands += 1
        return num_of_islands
    
    def dfs(self, i, j, grid, visited):
        m, n = len(grid), len(grid[0])
        queue = deque([(i, j)])
        visited[i][j] = True
        while len(queue):
            for _ in range(len(queue)):
                curr_x, curr_y = queue.popleft()
                for dx, dy in DIRECTIONS:
                    next_x, next_y = curr_x + dx, curr_y + dy
                    if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                        continue
                    if visited[next_x][next_y]:
                        continue
                    if grid[next_x][next_y] == '1':
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))