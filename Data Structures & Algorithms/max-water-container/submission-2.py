class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l = 0 
        r = len(heights) - 1

        while l < r:
            dist = r - l
            minHeight = min(heights[l], heights[r])
            newArea = minHeight * dist
            area = max(area, newArea)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return area


