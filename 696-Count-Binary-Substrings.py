class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0

        mid = len(s) // 2
        while mid > 0:
            substr = '0' * mid + '1' * mid
            if s.count(substr) > 0:
                res += s.count(substr)
            mid -= 1
        
        mid = len(s) // 2
        while mid > 0:
            substr = '1' * mid + '0' * mid
            if s.count(substr) > 0:
                res += s.count(substr)
            mid -= 1
            
        return res

'''
Explanation
First, I count the number of 1 or 0 grouped consecutively.
For example "0110001111" will be [1, 2, 3, 4].

Second, for any possible substrings with 1 and 0 grouped consecutively, the number of valid substring will be the minimum number of 0 and 1. For example "0001111", will be min(3, 4) = 3, ("01", "0011", "000111")


Complexity
Time O(N)
Space O(1)
'''

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res   = []
        cur   = s[0]
        count = 1
        for i in range(1, len(s)):
            if s[i] == cur:
                count += 1
            else:
                cur = s[i]
                res.append(count)
                count = 1
                
        res.append(count)        
        
        res_final = 0
        for i in range(1, len(res)):
            res_final += min(res[i - 1], res[i])
        
        return res_final
