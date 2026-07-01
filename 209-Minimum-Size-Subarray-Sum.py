class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = len(nums) + 1
        cur_sum = 0
        left, right = 0, 0
        while right < len(nums):
            
            # Keep adding array elements while current
            while right < len(nums) and cur_sum < target:
                cur_sum += nums[right]
                right   += 1
            
            # If current sum >= target keep removing the elements
            while cur_sum >= target and left < len(nums):
                min_len = min(min_len, right - left)
                
                cur_sum -= nums[left]
                left += 1
        
        # print(left, right, cur_sum)
        
        return 0 if min_len == len(nums) + 1 else min_len


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        presum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            presum[i] = presum[i-1] + nums[i-1]
        left, right = 0, 1
        res = sys.maxsize
        while right < len(nums) + 1:
            if presum[right] - presum[left] < target:
                right += 1
            else:
                res = min(res, right - left)
                left += 1
        return 0 if res == sys.maxsize else res