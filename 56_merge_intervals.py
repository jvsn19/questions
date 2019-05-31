# Complexity:
# Time: O(N*logN)
# Space: O(N)

class Solution:
    def merge(self, intervals):
        intervals.sort()
        answer = []
        
        for (start, end) in intervals:
            if not answer:
                answer.append([start, end])
            
            else:
                # Check intersection
                top_start, top_end = answer[~0]
                if start <= top_end: # Intersection found
                    answer.pop()
                    answer.append([top_start, max(top_end, end)])
                else:
                    answer.append([start, end])
                    
        return answer