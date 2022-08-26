import collections

class Solution:
    def originalDigits(self, s: str) -> str:
        word_dict = collections.Counter(s)
        res = []

        # count 0
        if 'z' in word_dict.keys():
            num = word_dict['z']
            res.extend([0] * num)
            
            word_dict['z'] -= num
            word_dict['e'] -= num
            word_dict['r'] -= num
            word_dict['o'] -= num
        
        # remove 2
        if 'w' in word_dict.keys():
            num = word_dict['w']
            res.extend([2] * num)

            word_dict['t'] -= num
            word_dict['w'] -= num
            word_dict['o'] -= num
        
        # remove 6
        if 'x' in word_dict.keys():
            num = word_dict['x']
            res.extend([6] * num)

            word_dict['s'] -= num
            word_dict['i'] -= num
            word_dict['x'] -= num

        # remove 8
        if 'g' in word_dict.keys():
            num = word_dict['g']
            res.extend([8] * num)

            word_dict['e'] -= num
            word_dict['i'] -= num
            word_dict['g'] -= num
            word_dict['h'] -= num
            word_dict['t'] -= num

        # remove 4
        if 'u' in word_dict.keys():
            num = word_dict['u']
            res.extend([4] * num)

            word_dict['f'] -= num
            word_dict['o'] -= num
            word_dict['u'] -= num
            word_dict['r'] -= num

        # remove 5 - contigent on 4
        if 'f' in word_dict.keys() and word_dict['f'] > 0:
            num = word_dict['f']
            res.extend([5] * num)

            word_dict['f'] -= num
            word_dict['i'] -= num
            word_dict['v'] -= num
            word_dict['e'] -= num

        # remove 7 - contigent on 5
        if 'v' in word_dict.keys() and word_dict['v'] > 0:
            num = word_dict['v']
            res.extend([7] * num)

            word_dict['s'] -= num
            word_dict['e'] -= num
            word_dict['v'] -= num
            word_dict['e'] -= num
            word_dict['n'] -= num

        # remove 3 - contigent
        if 't' in word_dict.keys() and word_dict['t'] > 0:
            num = word_dict['t']
            res.extend([3] * num)

            word_dict['t'] -= num
            word_dict['h'] -= num
            word_dict['r'] -= num
            word_dict['e'] -= num
            word_dict['e'] -= num
            
        # remove 1 - contigent
        if 'o' in word_dict.keys() and word_dict['o'] > 0:
            num = word_dict['o']
            res.extend([1] * num)

            word_dict['o'] -= num
            word_dict['n'] -= num
            word_dict['e'] -= num

        # remove 9 - contigent
        if 'i' in word_dict.keys() and word_dict['i'] > 0:
            num = word_dict['i']
            res.extend([9] * num)

            word_dict['n'] -= num
            word_dict['i'] -= num
            word_dict['n'] -= num
            word_dict['e'] -= num

        res = sorted(res)
        res = [str(i) for i in res]
        return ''.join(res)