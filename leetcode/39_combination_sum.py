class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = []
        
        def helper(idx = 0, curr_sum = 0, curr_elements = []):
            if curr_sum >= target:
                if curr_sum == target:
                    self.answer.append(curr_elements)
                return
                    
            for i in range(idx, len(candidates)):
                helper(i, curr_sum + candidates[i], curr_elements + [candidates[i]])
                
        helper()
        return self.answer