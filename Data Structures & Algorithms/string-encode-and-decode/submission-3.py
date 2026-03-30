class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        if len(strs) == 0:
            return ""

        for word in strs:
            res.append(f"##^#{word}")
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        res = []
        if len(s) == 0:
            return res

        return s.split("##^#")[1:]
            
