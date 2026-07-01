class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left + 1 < right:            
            
            # remove the duplicated ones
            # duplicated ones are at left-side
            while left + 1 < right and nums[left] == nums[left + 1]:
                left += 1
            # duplicated ones are at right-side
            while left + 1 < right and nums[right] == nums[right - 1]:
                right -= 1
            # duplicated ones are at left- and right-sides
            while left + 1 < right and nums[left] == nums[right]:
                right -= 1

            # safe to return if there are only 2 elements left
            if left + 1 == right:
                return nums[left] if nums[left] < nums[right] else nums[right]

            # monotonely increasing array
            if nums[right] > nums[left]:
                return nums[left]

            mid = (left + right) // 2
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid
        
        return nums[left] if nums[left] < nums[right] else nums[right]
