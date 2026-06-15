class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = -1
        while left < right:
            bredth = right - left
            length = min(heights[right], heights[left])
            area = bredth * length

            if max_area < area:
                max_area = area
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
            

        




