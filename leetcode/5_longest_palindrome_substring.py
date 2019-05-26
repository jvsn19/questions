class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                
            return s[left + 1 : right]
        
        answer = ''
        
        for i in range(len(s)):
            expand_odd = expand_center(i,i)
            expand_even = expand_center(i, i+1)
            
            if len(expand_odd) > len(answer):
                answer = expand_odd
                
            if len(expand_even) > len(answer):
                answer = expand_even
                
        return answer
            