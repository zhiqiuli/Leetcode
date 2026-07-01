class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            # monotonely increasing array, the smallest one is the right-most one
            if nums[right] > nums[left]:
                return nums[left]
            mid = (left + right) // 2
            target = nums[mid]
            # the minimum value is on the right-side of the target
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid
        return nums[left] if nums[left] < nums[right] else nums[right]