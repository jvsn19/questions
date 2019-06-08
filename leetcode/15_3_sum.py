# Complexity
# Time: O(N^2)
# Space: O(1) (or O(N) considering the answer and the space of sort)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size_nums = len(nums)
        nums.sort()
        answer = []
        
        for idx_a, val_a in enumerate(nums):
            if idx_a and nums[idx_a - 1] == nums[idx_a]:
                continue

            left, right = idx_a + 1, size_nums - 1
            
            while left < right:
                values = [val_a, nums[left], nums[right]]
                
                if sum(values) == 0:
                    answer.append(values)

                    while left < right and nums[left] == nums[left + 1]: left += 1
                    while left < right and nums[right] == nums[right - 1]: right -= 1
                        
                    left += 1
                    right -= 1
                    
                elif sum(values) > 0:
                    right -= 1
                    
                else:
                    left += 1
                    
        return answer