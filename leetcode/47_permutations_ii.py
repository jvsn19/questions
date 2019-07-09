class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        
        def helper(remaining_nums = nums, curr_nums = []):
            if len(curr_nums) == len(nums):
                self.answer.append(curr_nums)
                return
            
            for i in range(len(remaining_nums)):
                if i == 0 or remaining_nums[i] != remaining_nums[i-1]:
                    helper(remaining_nums[:i] + remaining_nums[i+1:], curr_nums + [remaining_nums[i]])
                
                
        nums.sort()
        helper()
        return self.answer