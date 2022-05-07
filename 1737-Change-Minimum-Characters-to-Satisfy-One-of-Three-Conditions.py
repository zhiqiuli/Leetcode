import collections
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        a_counter = collections.Counter([ord(i) - ord('a') for i in a])
        b_counter = collections.Counter([ord(i) - ord('a') for i in b])
        ret = sys.maxsize
        for th in range(26):
            
            # boundary不可能是'a'
            if th > 0:
                
                # 对应条件1
                change = 0
                # 改变所有小于th需要的步骤
                for i in range(th):
                    change += a_counter[i]
                # 改变所有大于th需要的步骤
                for i in range(th, 26):
                    change += b_counter[i]
                ret = min(ret, change)

                change = 0
                for i in range(th):
                    change += b_counter[i]
                for i in range(th, 26):
                    change += a_counter[i]
                ret = min(ret, change)
            
            change = 0
            for i in range(26):
                if i != th:
                    change += a_counter[i]
                    change += b_counter[i]
            ret = min(ret, change)
            
        return ret
