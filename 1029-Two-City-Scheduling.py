class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        if not costs or not costs[0]:
            return 0
        
        N = len(costs)
        n = N // 2
        
        diff = [(i[0] - i[1], j) for (i, j) in zip(costs, range(N))]
        diff = sorted(diff)

        res = 0

        print(diff)

        # [[10,20],[30,200],[400,50],[30,20]]
        # [(-170, 1), (-10, 0), (10, 3), (350, 2)]
        #  -- 1th ppl (30, 200) goes to A is better

        # 1st half ppl go to A
        for i in range(n):
            ppl = diff[i][1]
            res += costs[ppl][0]
        
        # 2nd half ppl go to B
        for i in range(n, N):
            ppl = diff[i][1]
            res += costs[ppl][1]
        
        return res