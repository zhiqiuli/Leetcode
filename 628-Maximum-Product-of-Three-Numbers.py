class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return max(nums[0 ] * nums[1 ] * nums[-1],  # 最大值是最后三个值之乘积
                   nums[-3] * nums[-2] * nums[-1],) # 最大值是前两个值和最后一个数乘积
