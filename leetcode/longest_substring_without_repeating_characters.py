# Complexity
# Time: O(N)
# Space: O(N)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_idx = {}
        global_answer = local_answer= start = 0
        
        for idx, char in enumerate(s):
            
            if char in chars_idx and chars_idx[char] >= start:
                start = chars_idx[char] + 1
                local_answer = idx - start + 1
                
            else:
                local_answer += 1
                global_answer = max(global_answer, local_answer)
                
            chars_idx[char] = idx
                
        return global_answer
                
            
