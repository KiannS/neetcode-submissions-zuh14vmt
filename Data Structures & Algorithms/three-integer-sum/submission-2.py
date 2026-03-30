class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j = i + 1
            r = len(nums) - 1
            while j < r:
                sum = nums[i] + nums[j] + nums[r]
                if sum == 0:
                    res.append([nums[i], nums[j], nums[r]])
                    while j < r and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1 
                    while r > j and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
                elif sum < 0:
                    while j < r and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1 
                elif sum > 0:
                    while r > j and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1 
        
        return res

                


        