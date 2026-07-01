import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = [(-nums[i], i) for i in range(k)]
        heapq.heapify(h)
        res = [-h[0][0]]
        for i in range(k, len(nums)):
            # NOTE: because the answer always includes nums[i], make sure *add first*
            heapq.heappush(h, (-nums[i], i))
            # i-k+1 is the beginning index for current window
            while h[0][1] < i-k+1:
                heapq.heappop(h)
            res.append(-h[0][0])
        return res