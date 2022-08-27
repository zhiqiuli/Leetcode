'''
Chinese Explanations:
所有活动按startDay排序
从第day=0天开始参加活动
min_heap里维护第day天可以参加的所有活动，所以在第day天前结束的活动需弹出
在第day天可以参加的所有活动中，优先参加endDay更早的活动（作者提供了证明）。
第day天参加了活动后，下一次在第day=day+1天参加。如果此时没有任何活动举办，则使用下一个活动的开始时间作为day
'''

import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        total_days = max(end for start, end in events)
        day = 0
        event_id = 0
        num_events_attended = 0
        min_heap = []
        
        for day in range(1, total_days+1):
            # Add all the events that start today
            # 或者加入今天可以参加的所有活动 events[i_event][0] <= day <= events[i_event][1]
            while event_id < len(events) and events[event_id][0] == day:
                heappush(min_heap, events[event_id][1])
                event_id += 1
            
            # Remove all the events whose end date was before today
            while min_heap and min_heap[0] < day:
                heappop(min_heap)
            
            # NOTE:这个地方用的是if，每天只能参加一个活动
            # if any event that can be attended today, let's attend it
            if min_heap:
               heappop(min_heap)
               num_events_attended += 1
                
        return num_events_attended
