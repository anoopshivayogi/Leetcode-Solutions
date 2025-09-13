class Solution:
    def maxFreqSum(self, s: str) -> int:
        
        # Solution 1 - 
        # Time - 
        # Space - 

        freq = Counter(s)
        max_v, max_c = 0, 0

        for c in s:
            if c in "aeiou":
                max_v = max(freq.get(c), max_v)
            else:
                max_c = max(freq.get(c), max_c)

        return max_v + max_c