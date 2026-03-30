class Solution:
    def trap(self, heights: List[int]) -> int:
        left = [0 for i in range(len(heights))]
        right = [0 for i in range(len(heights))]
        leftMax = 0
        rightMax = 0
        total = 0

        for i in range (len(heights)):
            leftMax = max(leftMax, heights[i])
            left[i] = leftMax
        for i in range(len(heights) - 1, -1, -1):
            rightMax = max(rightMax, heights[i])
            right[i] = rightMax
        for i in range (len(heights)):
            water = min(left[i], right[i]) - heights[i]
            if water < 0:
                continue
            total += water
        return total

        



        