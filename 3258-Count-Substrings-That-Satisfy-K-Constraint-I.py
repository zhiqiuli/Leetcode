class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res = 0
        num_1s = num_0s = 0
        left = 0
        for right, c in enumerate(s):
            if c == '1':
                num_1s += 1
            else:
                num_0s += 1
        
            # move the left pointer s.t. neither conditions are not met
            while num_1s > k and num_0s > k:
                if s[left] == '1':
                    num_1s -= 1
                else:
                    num_0s -= 1
                left += 1
            
            # left, left+1, ..., right (number of substrings ending i is right - left + 1)
            res += (right - left + 1)
        
        return res