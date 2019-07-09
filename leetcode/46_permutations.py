class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        size_nums = len(nums)
        
        def helper(mask = 0, permutation = []):
            if len(permutation) == size_nums:
                self.answer.append(permutation)
                
            for idx, elem in enumerate(nums):
                if not (mask & 1<<idx):
                    helper(mask | 1 << idx, permutation + [elem])
                
        helper()
        return self.answer