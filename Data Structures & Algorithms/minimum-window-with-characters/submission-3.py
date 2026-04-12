class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if len(t) > len(s):
            return ""
        if s == t:
            return s

        counts_t = {}
        windowMap = {}
        l = 0 
        count = 0

        for char in t:
            counts_t[char] = counts_t.get(char, 0) + 1       
        for r in range(len(s)):
            windowMap[s[r]] = windowMap.get(s[r], 0) + 1
            if s[r] in counts_t and windowMap[s[r]] == counts_t[s[r]]:
                count += 1
            while count == len(counts_t):
                if r - l + 1 < len(res) or res == "":
                    res = s[l: r + 1]
                windowMap[s[l]] -= 1
                if s[l] in counts_t and windowMap[s[l]] < counts_t[s[l]]:
                    count -= 1
                l += 1

        return res

            
            



        