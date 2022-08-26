class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        res = []
        diff = sys.maxsize
        for i in range(1, len(arr)):
            cur_diff = arr[i] - arr[i - 1]
            if cur_diff == diff:
                res.append([arr[i - 1], arr[i]])
            elif cur_diff < diff:
                res = [[arr[i - 1], arr[i]]]
                diff = cur_diff
            else:
                continue
        return res