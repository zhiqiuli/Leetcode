class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        res = 0
        m = 1
        while 2 * n - m * m + m  > 0:
            if (2 * n - m * m + m) % (2 * m) == 0:
                res += 1
            m += 1
        return res