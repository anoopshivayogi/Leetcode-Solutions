class Solution:
    def reverseDegree(self, s: str) -> int:
        

        res = 0
        pos = 1

        for ch in s:
            res += pos * (26 - (ord(ch) - ord('a')))
            pos += 1

        return res