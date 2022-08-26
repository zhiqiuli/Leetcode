import collections

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        counter_pair = [[key, counter[key]] for key in counter.keys()]
        counter_pair = sorted(counter_pair, key=lambda x:x[1])
        
        num_removed = 0
        for pair in counter_pair:
            if k >= pair[1]:
                num_removed += 1
                k -= pair[1]
            else:
                return len(counter_pair) - num_removed 
        return len(counter_pair) - num_removed