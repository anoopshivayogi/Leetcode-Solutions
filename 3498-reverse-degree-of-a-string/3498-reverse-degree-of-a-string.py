class Solution:
    def reverseDegree(self, s: str) -> int:

        # Solution
        # Time - O(n)
        # Space - O(1)
        

        res = 0

        for idx, ch in enumerate(s, start=1):
            res += idx * (26 - (ord(ch) - ord('a')))

        return res