class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = -1
        while l < r:
            area = max(area, min(height[l], height[r]) * (r - l))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return area