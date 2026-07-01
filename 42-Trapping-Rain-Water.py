class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        left_max, right_max = [0] * n, [0] * n
        for i in range(n):
            left_max[i] = max(height[:i+1])
        for i in range(n - 1, -1, -1):
            right_max[i] = max(height[i:])
        res = 0
        for i in range(1, n - 1):
            res += (min(left_max[i], right_max[i]) - height[i])
        return res



class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        res = 0
        while l < r:
            if l_max > r_max:
                r -= 1
                res += max(0, r_max - height[r])
                r_max = max(r_max, height[r])
            else:
                l += 1
                res += max(0, l_max - height[l])
                l_max = max(l_max, height[l])
        return res