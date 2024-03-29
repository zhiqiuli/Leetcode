class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.dfs(s, p, 0, 0, {})
    
    def dfs(self, s, p, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        
        # exit 1 when s is emtpy
        if s[i:] == '':
            if p[j:] == '':
                return True
            return len(set(p[j:])) == 1 and p[j] == '*'
        
        # exit 2 when p is empty
        if p[j:] == '':
            return s[i:] == ''
        
        if p[j] != '*':
            matched = (s[i] == p[j] or p[j] == '?') and self.dfs(s, p, i + 1, j + 1, memo)
        else:
            matched = self.dfs(s, p, i, j + 1, memo) or self.dfs(s, p, i + 1, j, memo)
        
        '''
        # another way to write the logic
        # 3 different cases are corresponding to 3 cases
        # * takes 1 position from s or takes no position from s
        if p[0] == '*':
            matched = self.dfs(s[1:], p, i+1, j, memo) or self.dfs(s, p[1:], i, j+1, memo)
        
        # ? always takes 1 position from s
        elif p[0] == '?':
            matched = self.dfs(s[1:], p[1:], i+1, j+1, memo)
        
        # compares the 1st elements in s and p and pass to next level
        else:
            matched = (s[0] == p[0]) and self.dfs(s[1:], p[1:], i+1, j+1, memo)
        '''
        
        memo[(i, j)] = matched
        return matched
