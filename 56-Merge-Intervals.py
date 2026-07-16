class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:(x[0], x[1])) # sort by first key (ascending), then second key (ascending)
        print(intervals)
        if len(intervals) == 1:
            return intervals
        l_prev = intervals[0][0]
        r_prev = intervals[0][1]
        res = []
        for interval in intervals[1:]:
            if r_prev >= interval[1]:
                continue
            elif r_prev >= interval[0]:
                r_prev = interval[1]
            else:
                res.append([l_prev, r_prev])
                l_prev = interval[0]
                r_prev = interval[1]
        res.append([l_prev, r_prev])
        return res