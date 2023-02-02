# Lintcode/154-Regular-Expression-Matching.py 
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.dfs(s, p, 0, 0, {})
        
    def dfs(self, s, p, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if s[i:] == '':
            return self.is_p_empty(p[j:])
        
        if p[j:] == '':
            return s[i:] == ''
        
        if j + 1 < len(p) and p[j+1] == '*':
            matched = self.dfs(s, p, i, j + 2, memo) or \
                      (s[i] == p[j] or p[j] == '.') and self.dfs(s, p, i + 1, j, memo)
        else:
            matched = (s[i] == p[j] or p[j] == '.') and self.dfs(s, p, i + 1, j + 1, memo)
            
        memo[(i,j)] = matched
        return matched
    
    # a*b*
    def is_p_empty(self, p):
        if len(p) % 2 == 1:
            return False
        for i in range(len(p) // 2):
            if p[2 * i + 1] != '*':
                return False
        return True