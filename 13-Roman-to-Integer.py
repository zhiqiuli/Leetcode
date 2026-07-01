class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        若存在(小的数字)在(大的数字)的(左边)的情况，根据规则需要减去小的数字。
        对于这种情况，我们也可以将每个字符视作一个单独的值，若一个数字右侧的数字比它大，则将该数字的符号取反。
        例如 XIV 可视作 X−I+V=10−1+5=14。
        '''
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if i < len(s) - 1 and d[s[i]] < d[s[i+1]]:
                res -= d[s[i]]
            else:
                res += d[s[i]]
        return res