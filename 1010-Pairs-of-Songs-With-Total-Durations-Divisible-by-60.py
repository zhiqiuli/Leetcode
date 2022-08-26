class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c = [0] * 61
        res = 0
        for t in time:
            m     = t % 60
            res  += c[60 - m]
            c[60 if m == 0 else m] += 1
        return res