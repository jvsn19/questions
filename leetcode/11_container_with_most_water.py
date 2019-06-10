class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0

        while left < right:
            width = right - left
            height = min(heights[right], heights[left])

            max_area = max(max_area, width * height)

            if heights[right] > heights[left]:
                left += 1

            else:
                right -= 1

        return max_area