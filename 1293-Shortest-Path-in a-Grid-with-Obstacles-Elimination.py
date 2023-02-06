from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0
        visited = set([(0,0,k)])
        q = deque([(0,0,k)])
        step = 0
        while q:
            step += 1
            for _ in range(len(q)):
                x, y, rest = q.popleft()
                for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                    nx, ny  = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 0:
                            if nx == m - 1 and ny == n - 1:
                                return step
                            if (nx, ny, rest) not in visited:
                                visited.add((nx, ny, rest))
                                q.append((nx, ny, rest))
                        elif grid[nx][ny] == 1:
                            if (nx, ny, rest - 1) not in visited and rest > 0:
                                visited.add((nx, ny, rest - 1))
                                q.append((nx, ny, rest - 1))
        return -1
