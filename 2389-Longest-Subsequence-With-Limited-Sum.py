class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums = sorted(nums)
        nums_sum = [0] * len(nums)
        nums_sum[0] = nums[0]
        for i in range(1, len(nums)):
            nums_sum[i] = nums_sum[i-1] + nums[i]
        
        res = []
        for q in queries:
            res.append(self.find_the_last(nums_sum, q) + 1)
            
        return res
    
    # last positon binary search 模版
    def find_the_last(self, nums, target):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
                
        if nums[right] <= target: return right
        if nums[left] <= target: return left
        
        return -1
    