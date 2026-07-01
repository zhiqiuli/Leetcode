'''
https://www.youtube.com/watch?v=HeFW6EPBGBg
subarray之和的题目转换为前缀和之差
{j,i} s.t. presum[i]-presum[j] >= k
遍历i，最优解找到j
O(N)，每个元素只会进一次/出一次deque
此题记图！！！
'''
from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # 首先计算presum
        presum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            presum[i] = presum[i-1] + nums[i-1]
        # deque维护一个monotonically increasing的数组s.t.
        # presum[queue[0]] > presum[queue[1]] > presum[queue[2]] ...
        # queue[0] <- queue[1] <- queue[2] <-...
        queue = deque()
        res = sys.maxsize
        for i in range(len(nums) + 1):
            # 从右侧pop，确保 ... < presum[queue[-1]] < presum[i]
            while len(queue) != 0 and presum[queue[-1]] >= presum[i]:
                queue.pop()
            # 找到满足条件的i和j，从左侧pop，缩小i和j的差距
            while len(queue) != 0 and presum[i] - presum[queue[0]] >= k:
                res = min(res, i - queue[0])
                queue.popleft()
            # 此时queue应是monotonically increasing
            queue.append(i)
        return -1 if res == sys.maxsize else res