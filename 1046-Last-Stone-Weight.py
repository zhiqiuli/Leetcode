class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        h = []
        for i in stones: heapq.heappush(h, -i)
        while len(h) > 1:            
            s1 = -heapq.heappop(h)
            s2 = -heapq.heappop(h)
            if s1 != s2:
                heapq.heappush(h, s2-s1)
        if len(h) == 0: return 0
        return -h[0]
