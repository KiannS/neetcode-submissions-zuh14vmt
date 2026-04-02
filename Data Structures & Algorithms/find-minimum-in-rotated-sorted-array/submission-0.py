class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')
        l = 0
        r = len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]

        while l <= r:
            mid = (l + r)// 2
            res = min(nums[mid], res)

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return res


            

        


        