class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x%10 == 0):
            return False
        
        reverted = 0
        aux_x = x
        
        while reverted < aux_x:
            reverted *= 10
            reverted += (aux_x % 10)
            aux_x //= 10
            
        return reverted == aux_x or reverted//10 == aux_x