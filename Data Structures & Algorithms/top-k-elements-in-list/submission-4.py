class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        map = defaultdict(int)
        res = []

        for num in nums:
            map[num] += 1
        
        for num, count in map.items():
            freq[count].append(num)
        
        for i in range(len(freq) - 1,0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res
            
            

