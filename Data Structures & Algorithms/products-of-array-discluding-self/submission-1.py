class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for r in range (len(nums))]
        suffix = [1 for r in range (len(nums))]
        res = [0 for k in range (len(nums))]

        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i - 1]
        
        for j in range(len(nums) - 2, -1, -1):
            suffix[j] = nums[j+1] * suffix[j+1]
        
        for k in range(len(res)):
            res[k] = suffix[k] * prefix[k]
        return res






        
        