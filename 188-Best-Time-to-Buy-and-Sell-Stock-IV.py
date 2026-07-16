class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buys  = [-prices[0]] * k
        sells = [0] * k
        for price in prices:
            for i in range(k):
                if i == 0:
                    buys [i] = max(buys [i],            - price)
                    sells[i] = max(sells[i],  buys[i]   + price)
                else:
                    buys [i] = max(buys [i],  sells[i-1] - price)
                    sells[i] = max(sells[i],  buys[i]    + price)
        return sells[-1]