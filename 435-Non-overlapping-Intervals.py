import heapq
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals, key=lambda x:x[1])
        
        num_of_overlap = 0
        
        cur_left, cur_right = intervals[0][0], intervals[0][1]
        
        for i in range(1, len(intervals)):
            
            if cur_right > intervals[i][0]:
                num_of_overlap += 1
            else:
                cur_left, cur_right = intervals[i][0], intervals[i][1]

        return num_of_overlap