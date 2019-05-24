# Complexity
# Time: O(n)
# Space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_nums = {}
        
        for idx, num in enumerate(nums):
            to_find = target - num
            
            if to_find in hash_nums:
                return [hash_nums[to_find], idx]
            
            hash_nums[num] = idx
            
