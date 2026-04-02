class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1

        if nums[l] < nums[r]:
            while l <= r:
                mid = (l +r)//2

                if nums[mid] == target:
                    return mid
                if target > nums[mid]:
                    l = mid +1
                if target < nums[mid]:
                    r = mid - 1
            return -1 

        while l <= r:
            mid = (l +r)//2
            leftSorted = False

            if target == nums[r]:
                return r
            if target == nums[l]:
                return l

            if nums[mid] == target:
                return mid        
            # check which side is sorted
            if nums[mid] > nums[l]:
                leftSorted = True
            if leftSorted:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            if not leftSorted:
                if target <= nums[r] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            
        return -1
        