# Option 1

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        AAA_count = 0
        BBB_count = 0
        for i in range(len(colors) - 2):
            if colors[i:i+3] == 'AAA':
                AAA_count += 1
            elif colors[i:i+3] == 'BBB':
                BBB_count += 1
            else:
                continue
        return AAA_count > BBB_count

        
# Option 2

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count_pairs = {}
        for i in range(len(colors) - 2):
            if colors[i:i+3] not in count_pairs:
                count_pairs[colors[i:i+3]] = 1
            else:
                count_pairs[colors[i:i+3]] += 1
        k = 0
        while True:
            if k % 2 == 0:
                if 'AAA' not in count_pairs or count_pairs['AAA'] == 0:
                    return False
                else:
                    count_pairs['AAA'] -= 1
            else:
                if 'BBB' not in count_pairs or count_pairs['BBB'] == 0:
                    return True
                else:
                    count_pairs['BBB'] -= 1
            k += 1
        return False