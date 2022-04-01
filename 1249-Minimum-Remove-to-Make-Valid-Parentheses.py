class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        extra_left  = []
        extra_right = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if len(stack) != 0:
                    stack.pop()
                else:
                    extra_right.append(i)
        extra_left = stack[:]
        res = ''
        for i, c in enumerate(s):
            if i not in extra_left and i not in extra_right:
                res += c
        return res
