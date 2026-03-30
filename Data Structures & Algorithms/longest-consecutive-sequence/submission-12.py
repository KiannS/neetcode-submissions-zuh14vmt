class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        map = defaultdict(int)
        res = 0

        for num in nums:
            if not num - 1 in numSet:
                map[num] = 1
        
        for num in map.keys():
            temp = num
            while temp + 1 in numSet:
                map[num] += 1
                temp += 1
        
        for count in map.values():
            res = max(res, count)
        
        return res

            