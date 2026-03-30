class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        if len(strs) == 0:
            return ""

        for word in strs:
            res.append(f"{len(word)}#{word}")
        return "".join(res)

        


    def decode(self, s: str) -> List[str]:
        res = []
        if len(s) == 0:
            return res

        i = 0
        while i < len(s):
            j = i

            while s[j] != '#' :
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j + 1 + length])  #  5#hello
            i = j + length + 1
        return res
            
