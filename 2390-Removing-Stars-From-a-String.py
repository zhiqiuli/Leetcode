class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        i = len(s) - 1
        queue = []
        while i >= 0:
            if s[i] == '*':
                queue.append('*')
                i -= 1
            else:
                if queue:
                    queue.pop()
                else:
                    res.append(s[i])
                i -= 1
        return ''.join(res[::-1])

# 从头到尾也可以
class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        i = 0
        while i < len(s):
            if s[i] != '*':
                res.append(s[i])
            else:
                res.pop()
            i += 1
        return ''.join(res)