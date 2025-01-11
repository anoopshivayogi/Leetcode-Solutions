class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        # Solution 1 - 
        # Time -
        # Space -

        freq = Counter(s)
        count = 0

        for key, val in freq.items():
            if val % 2 == 1:
                count += 1

        if count <= k:
            if len(s) >= k:
                return True
            if count == k:
                return True

        return False