class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        return [self.checkPattern(word, pattern) for word in queries]

    def checkPattern(self, word, pattern):
        i, j = 0, 0
        
        while i < len(word) and j < len(pattern):
            
            # exactly matched
            if word[i] == pattern[j]:
                i += 1
                j += 1
                continue
            
            # skip the lower case
            if word[i].islower():
                i += 1
                continue
            
            if word[i] != pattern[j]:
                return False
                
        while j < len(pattern):
            return False
        
        while i < len(word):
            if word[i].isupper():
                return False
            i += 1
                
        return True