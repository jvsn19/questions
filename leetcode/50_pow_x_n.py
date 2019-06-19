class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(base, expo):
            negative_expo = (expo < 0)
            expo = abs(expo)
            answer = 1.0
            
            while expo:
                
                if expo & 1:
                    answer *= base
                    
                base *= base
                expo >>= 1
                
            return 1/answer if negative_expo else answer 
                
        return helper(x, n)