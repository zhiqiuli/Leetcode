class Solution:
    def minimizeResult(self, expression: str) -> str:

        exp_list = expression.split('+')
        exp_part1 = exp_list[0]
        exp_part2 = exp_list[1]

        min_val = sys.maxsize
        min_key = ''

        for i in range(len(exp_part1)):
            for j in range(1, len(exp_part2) + 1):
                key = exp_part1[:i] + '(' + exp_part1[i:] + \
                '+' + exp_part2[:j] + ')' + exp_part2[j:]
                val = self.evaluate(key)

                if val < min_val:
                    min_val = val
                    min_key = key
        return min_key

    
    def evaluate(self, expression):
        
        index1 = expression.index('(')
        index2 = expression.index('+')
        index3 = expression.index(')')

        a2 = int(expression[index1 + 1:index2]) + int(expression[index2 + 1:index3])

        a1 = 1 if expression[:index1] == '' else int(expression[:index1])
        a3 = 1 if expression[index3 + 1:] == '' else int(expression[index3 + 1:])
        
        return a1 * a2 * a3