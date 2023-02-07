class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        return self.is_matched(pattern, s, {}, set())

    def is_matched(self, pattern, string, mapping, used):
        # pattern is empty then string should be empty
        # this is also the ending condition
        if not pattern:
            return not string
        
        # take 1st element in the pattern
        char = pattern[0]

        # char存在mapping中，如果string以mapping[char]开头，则进行下一层搜索；
        # 如果string不以mapping[char]开头，则返回False
        if char in mapping:
            word = mapping[char]
            if not string.startswith(word):
                return False
            return self.is_matched(pattern[1:], string[len(word):], mapping, used)
        
        # 搜索不同的可能性a:r, a:re, a:red, a:red...
        for i in range(len(string)):
            word = string[:i+1]
            if word in used:
                continue
            
            used.add(word)
            mapping[char] = word

            if self.is_matched(pattern[1:], string[i+1:], mapping, used):
                return True
            
            used.remove(word)
            del mapping[char]