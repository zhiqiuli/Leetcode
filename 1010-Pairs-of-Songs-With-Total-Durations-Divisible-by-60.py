class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c = {}
        res = 0
        for t in time:
            rem = t % 60
            
            # 存在配对的情况
            # 存在60-rem=60的情况，需要再次%60让key回到0~59
            if (60 - rem) % 60 in c:
                res += c[(60 - rem) % 60]
            
            # 保存余数，此时c的key范围总是0~59
            if rem not in c:
                c[rem] = 1
            else:
                c[rem] += 1
        print(c)
        return res



from collections import Counter
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c = Counter([t % 60 for t in time])
        print(c)
        res = 0
        res += (c[0]  * (c[0] - 1 )) // 2
        res += (c[30] * (c[30] - 1)) // 2
        res += sum([c[i] * c[60 - i] for i in range(1, 30)])
        return res