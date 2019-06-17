class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(idx = 0, curr_elem = [], curr_sum = 0):
            if curr_sum >= target:
                if curr_sum == target:
                    self.answer.append(curr_elem)
                return
            
            for i in range(idx, len(candidates)):
                if idx != i and candidates[i] == candidates[i-1]:
                    continue
                if idx == 0:
                    print(candidates[i])
                helper(i + 1, curr_elem + [candidates[i]], curr_sum + candidates[i])
        
        self.answer = []
        candidates.sort()
        helper()
        
        return self.answer
        