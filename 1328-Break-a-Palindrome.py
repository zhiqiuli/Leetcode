class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        
        mid = len(palindrome) // 2
        
        res   = []
        found = False
        for i in range(mid):
            
            if found:
                res.append(palindrome[i])
                continue
            
            # skip all a
            if palindrome[i] == 'a':
                res.append(palindrome[i])
                continue
            # find the char that needs to be replaced
            else:
                res.append('a')
                found = True
        
        # which means all a's
        if not found:
            return palindrome[:-1] + 'b'
        
        return ''.join(res) + ''.join(palindrome[mid:])