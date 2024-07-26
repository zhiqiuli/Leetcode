class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = 0
        d = [0, 1] # 这个向量代表了起始方向
        for c in instructions:
            if c == 'G':
                x, y = x + d[0], y + d[1]
            elif c == 'L': # 向左转
                d[0], d[1] = -d[1], d[0]
            elif c == 'R': # 向右转
                d[0], d[1] =  d[1], -d[0]
            else:
                continue
        # 情况1 机器人还在原地
        # 情况2 机器人结束的方向和起始的方向不一致，就不会越走越远
        return (x == y == 0) or (d != [0, 1])
