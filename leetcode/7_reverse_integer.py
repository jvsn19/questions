class Solution:
    def reverse(self, x: int) -> int:
        LIMITS = (-2**31, 2**31 - 1)
        
        is_negative = x < 0
        x = abs(x)
        new_x = 0
        
        while x:
            new_x *= 10
            new_x += x%10
            x //= 10
            
        new_x = -new_x if is_negative else new_x
            
        return new_x if LIMITS[0] <= new_x <= LIMITS[1] else 0