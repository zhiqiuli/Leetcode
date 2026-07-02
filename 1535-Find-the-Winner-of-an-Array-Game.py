class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner = arr[0]
        winTimes = 0
        for i in range(1, len(arr)):
            if arr[i] > winner:
                winner = arr[i]
                winTimes = 1
            else:
                winTimes +=1

            if winTimes >= k:
                return winner
        
        return winner