class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cumsum = [0] * len(nums)
        cumsum[0] = nums[0]
        for i in range(1, len(nums)):
            cumsum[i] = nums[i] + cumsum[i - 1]
        if min(cumsum) <= 0:
            return abs(min(cumsum)) + 1
        else:
            return 1