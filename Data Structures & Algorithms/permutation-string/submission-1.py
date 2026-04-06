class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_map = defaultdict(int)
        s2_map = defaultdict(int)

        for char in s1:
            s1_map[char] += 1
        for i in range(len(s1)):
            s2_map[s2[i]] += 1  
        if s1_map == s2_map:
            return True
        l = 0
        r = l + len(s1)
        while r < len(s2):
            s2_map[s2[l]] -= 1
            if s2_map[s2[l]] == 0:
                s2_map.pop(s2[l])
            l += 1
            r += 1
            s2_map[s2[r - 1]] += 1
            if s1_map == s2_map:
                return True
        return False


        


        