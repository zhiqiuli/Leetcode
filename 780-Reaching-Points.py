###
### BFS but MLE
###
from collections import deque
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        queue = deque([(sx, sy)])
        visited = set((sx, sy))
        while queue:
            for _ in range(len(queue)):
                currPoint = queue.popleft()
                # print('curent',currPoint)
                # check it is found
                if currPoint == (tx, ty):
                    return True
                for nextPoint in self.nextPoints(currPoint):
                    # print('next',nextPoint)
                    if nextPoint[0] > tx or nextPoint[1] > ty or nextPoint in visited:
                        continue
                    queue.append(nextPoint)
                    visited.add(nextPoint)
        return False

    def nextPoints(self, currPoint):
        sx, sy = currPoint[0], currPoint[1]
        return [(sx     , sx + sy),
                (sx + sy, sy     )]


