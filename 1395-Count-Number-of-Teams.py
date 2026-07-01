class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        res = 0
        for j in range(1, n - 1):
            l_total, r_total = j, n - j - 1 # j的左边一共有j个人，j的右边一共有n-j-1个人
            l, r = 0, 0 # j的左边有l个比j小，r个比j大
            for i in range(j):
                if rating[i] < rating[j]:
                    l += 1
            for k in range(j + 1, n):
                if rating[j] < rating[k]:
                    r += 1
            # 升序一共是(l * r)个combinations，降序一共是(r_total - r)个combinations
            res += (l * r) + (l_total - l) * (r_total - r)
        return res