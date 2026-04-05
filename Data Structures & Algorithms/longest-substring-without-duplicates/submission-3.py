class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        r = 1
        length = 1
        seen = set()
        seen.add(s[l])

        while r < len(s):
            while  r < len(s) and not s[r] in seen:
                length = max(r - l + 1, length)
                seen.add(s[r])
                r += 1
            seen.remove(s[l])
            l += 1
        return length
            
