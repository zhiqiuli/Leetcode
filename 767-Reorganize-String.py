from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        queue = [(-item[1], item[0]) for item in counter.items()]
        maxCounter = max([item[1] for item in counter.items()])
        if maxCounter > (len(s) + 1) // 2:
            return ''
        heapq.heapify(queue)
        ans = []
        
        while len(queue) > 1:
            _, char1 = heapq.heappop(queue)
            _, char2 = heapq.heappop(queue)
            ans.append(char1)
            ans.append(char2)
            counter[char1] -= 1
            counter[char2] -= 1
            if counter[char1] > 0:
                heapq.heappush(queue, (-counter[char1], char1))
            if counter[char2] > 0:
                heapq.heappush(queue, (-counter[char2], char2))

        if queue:
            ans.append(queue[0][1])
        
        return ''.join(ans)