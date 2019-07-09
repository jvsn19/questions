class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        new_ptr = 0
        
        for idx, num in enumerate(nums):
            nums[idx], nums[new_ptr] = nums[new_ptr], nums[idx]
            
            if num != val:
                new_ptr += 1
                
        return new_ptr

# Alternative Solution

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        st, end = 0, len(nums) - 1
        
        while st <= end:
            while end > st and nums[end] == val:
                end -= 1
                
            if nums[st] == val:
                nums[st], nums[end] = nums[end], nums[st]
                end -= 1
                
            st += 1
            
        return end + 1