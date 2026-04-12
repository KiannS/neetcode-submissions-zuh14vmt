class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        windowMax = nums[0]

        l = 0
        while l <= len(nums) - k:
            windowMax = nums[l]
            for r in range(l, l + k):
                windowMax = max(windowMax, nums[r])
            res.append(windowMax)
            l += 1
        return res


        