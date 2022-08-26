class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x:x[1], reverse=True)
        curLoad = 0
        for box in boxTypes:
            if box[0] <= truckSize:
                curLoad   += (box[0] * box[1])
                truckSize -=  box[0]
            else:
                curLoad   += (truckSize * box[1])
                return curLoad
        return curLoad