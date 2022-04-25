class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        extra_left  = [] # 记录多余的(的位置
        extra_right = [] # 记录多余的)的位置
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
