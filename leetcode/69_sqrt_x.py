class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x <= 1:
            return x
        
        def binary_search(target, left, right):
            
            while left < right:
                mid = (left + right)//2
                
                if mid*mid <= target:
                    left = mid + 1
                    
                else:
                    right = mid
                    
            return left - 1
        
        return binary_search(x, 0, x//2+1)