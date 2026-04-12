import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []

        l = 0
        for r in range(l, l + k):
            heapq.heappush(heap, (-1*nums[r], r))
        res.append(-1*heap[0][0])
        l = 1
        r += 1

        while l <= len(nums) - k:
            heapq.heappush(heap, (-1*nums[r], r))
            idx = heap[0][1]
            while not l <= idx <= r:
                heapq.heappop(heap)
                idx = heap[0][1]
            res.append(-1*heap[0][0])
            l += 1
            r += 1         
        return res


        