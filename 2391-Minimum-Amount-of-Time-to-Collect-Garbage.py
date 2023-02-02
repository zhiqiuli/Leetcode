class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel = [0] + travel
        p = self.calTotalTimeType(garbage, travel, 'P')
        g = self.calTotalTimeType(garbage, travel, 'G')
        m = self.calTotalTimeType(garbage, travel, 'M')
        return p + g + m
    
    
    def calTotalTimeType(self, garbage, travel, kind):
        total_num = 0
        time_per_stop = [g.count(kind) for g in garbage]
        t = len(time_per_stop) - 1
        while t >= 0 and time_per_stop[t] == 0:
            t -= 1
        while t >= 0:
            total_num += (time_per_stop[t] + travel[t])
            t -= 1
        return total_num