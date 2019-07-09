class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size_nums = len(nums)
        
        idx = 0
        
        while idx < size_nums:
            if nums[idx] == idx + 1 or not (0 < nums[idx] <= size_nums) or nums[nums[idx] - 1] == nums[idx]:
                idx += 1
            
            else:
                nums[nums[idx] - 1], nums[idx] = nums[idx], nums[nums[idx] - 1]
                
                
        print(nums)
        for idx, num in enumerate(nums):
            if num != idx + 1:
                return idx + 1
            
        return size_nums + 1