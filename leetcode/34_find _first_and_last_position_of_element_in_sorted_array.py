class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1, -1]
        
        def binary_search(target, leftmost, left, right):
            
            while left < right:
                mid = (left + right)//2
                
                if (nums[mid] < target and leftmost) or (nums[mid] <= target and not leftmost):
                    left = mid + 1
                    
                else:
                    right = mid
                
            return left if leftmost else left - 1
        
        left = binary_search(target, True, 0, len(nums))
        right = binary_search(target, False, 0, len(nums))
        
        return [left if nums[right] == target else -1,
               right if nums[right] == target else -1]