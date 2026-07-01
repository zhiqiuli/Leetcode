###
### SOLUTION 1
###
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # [1,(2),3,4,5]
        # [1,3,(4),5]
        # [1,3,5]
        # [(3),5]
        # [3]
        i = 0
        cands = [i for i in range(1, n+1)]
        while len(cands) > 1:
            i = (i + k - 1) % len(cands) # len(cands)是关键，可以保证i不超出范围
            cands.pop(i)
        return cands.pop()

###
### SOLUTION 2
###
from collections import deque
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # 1<-2<-3<-4<-5
        queue = deque([])
        for i in range(1, n + 1):
            queue.append(i)
        while len(queue) > 1:
            # 1<-2<-3<-4<-5 ==> 2<-3<-4<-5<-1
            for _ in range(k - 1):
                queue.append(queue.popleft())
            # 3<-4<-5<-1
            queue.popleft()
        return queue.popleft()