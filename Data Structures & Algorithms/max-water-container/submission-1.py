class Solution:
    def maxArea(self, heights: List[int]) -> int:
        N = len(heights)
        l = 0
        r = N - 1
        maxArea = 0

        while l < r:
            minheight = min(heights[l], heights[r])
            width = r - l 
            area = minheight * width
            maxArea = max(area, maxArea)
            
            if minheight == heights[l]:
                l += 1
            else:
                r -= 1
        return maxArea