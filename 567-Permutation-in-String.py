class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2: return False
        # NOTE: 使用list代替dict，让程序更简洁
        # 如果使用dict，还需要考虑val等于0时删掉相应的key
        count1, count2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        if count1 == count2:
            return True
        for i in range(n1, n2):
            count2[ord(s2[i]) - ord('a')] += 1
            count2[ord(s2[i - n1]) - ord('a')] -= 1
            if count1 == count2:
                return True
        return False