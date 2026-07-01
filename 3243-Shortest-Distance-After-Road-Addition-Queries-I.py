class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = {i:[i+1] for i in range(n)}
        # dist to last point
        dists = [n-i-1 for i in range(n)]
        res = []
        for query in queries:
            start, end = query[0], query[1]
            # add the new path
            graph[start].append(end)
            # select the minimum amongst the next ones
            for i in range(start, -1 ,-1):
                dists[i] = 1 + min([dists[k] for k in graph[i]])
            res.append(dists[0])
        return res