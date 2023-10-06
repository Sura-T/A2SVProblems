class Solution:
    def reverse(self, x: int) -> int:
        reversed_value = 0
        is_negative = False
        
        if x < 0:
            is_negative = True
            x = abs(x)
        
        while x != 0:
            digit = x % 10
            x = x // 10
            reversed_value = (reversed_value * 10) + digit
            
            if reversed_value > 2**31 - 1:
                return 0
        
        if is_negative:
            reversed_value *= -1
        
        return reversed_value