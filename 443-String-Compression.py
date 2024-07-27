class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars: return 0
        prev_char = chars[0]
        count = 1
        p = 0
        for c in chars[1:]:
            if c != prev_char:
                if count == 1:
                    chars[p] = prev_char
                    p += 1
                else:
                    chars[p] = prev_char
                    p += 1
                    for i in range(len(str(count))):
                        chars[p] = str(count)[i]
                        p += 1
                count = 1
                prev_char = c
            else:
                count += 1

        if count == 1:
            chars[p] = chars[-1]
            p += 1
        else:
            chars[p] = chars[-1]
            p += 1
            for i in range(len(str(count))):
                chars[p] = str(count)[i]
                p += 1
        
        return p
