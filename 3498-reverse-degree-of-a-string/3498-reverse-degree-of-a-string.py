class Solution:
    def reverseDegree(self, s: str) -> int:
        

        res = 0

        for idx, ch in enumerate(s, start=1):
            res += idx * (26 - (ord(ch) - ord('a')))

        return res