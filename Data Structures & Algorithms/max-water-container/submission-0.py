class Solution:
    def maxArea(self, heights: List[int]) -> int:
        N = len(heights)
        left = 0
        right = N - 1
        maxArea = 0
        while left < right:
            length = right - left
            minheight = min(heights[left], heights[right])
            area =  length * minheight
            maxArea = max(maxArea, area)

            if minheight == heights[left]:
                left += 1
            else:
                right -= 1
        
        return maxArea
        