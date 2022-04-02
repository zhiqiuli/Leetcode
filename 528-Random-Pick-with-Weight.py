import numpy as np

class Solution:

    def __init__(self, w: List[int]):
        self.cdf = np.cumsum([i / sum(w) for i in w])

    def pickIndex(self) -> int:
        p = np.random.uniform(0, 1)
        # return bisect.bisect_left(self.cdf, p) # Use build-in bisection function
        return self.bisection(self.cdf, p) # Write a bisection function
    
    def bisection(self, a, target):
        left, right = 0, len(a) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if a[mid] >= target:
                right = mid
            else:
                left = mid
        if a[left] >= target:
            return left
        if a[right] >= target:
            return right
        return None

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
