class Solution:
    def encode(self, strs: list[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.index("#", i)       # find the delimiter
            length = int(s[i:j])      # read the length
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length        # advance past this word
        return res