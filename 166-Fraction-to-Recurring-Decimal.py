class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return '0'
        
        negative_sign = '-' if numerator * denominator < 0 else ''

        numerator   = abs(numerator)
        denominator = abs(denominator)

        num = numerator // denominator
        rem = numerator % denominator

        if rem == 0:
            return negative_sign + str(num)
        
        reminders_seen = {} # this needs to be a dict to save where the repeated decimal starts
        decimals = []
        while rem:
            
            if str(rem) in reminders_seen:
                index = reminders_seen[str(rem)]
                # then break the unrepeated part and repeated part
                return negative_sign + str(num) + '.' + ''.join(decimals[:index]) + '(' + ''.join(decimals[index:]) + ')'
            
            reminders_seen[str(rem)] = len(reminders_seen)
            rem *= 10
            decimals.append(str(rem//denominator))
            rem %= denominator
        
        return negative_sign + str(num) + '.' + ''.join(decimals)
