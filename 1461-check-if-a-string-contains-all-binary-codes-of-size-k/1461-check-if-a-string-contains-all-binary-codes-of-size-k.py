class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
  # {00, 01, 11, 10}.  2^k = 4

        seen = set()
        target = 2**k
        n = len(s)
        for i in range(n):
            if i+k <= n:
                seen.add(s[i: i+k])
            if len(seen) == target:
                return True
        print(seen)
        return False