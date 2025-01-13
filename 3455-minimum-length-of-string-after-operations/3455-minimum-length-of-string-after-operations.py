class Solution:
    def minimumLength(self, s: str) -> int:
        
        
        # Solution 1 - using frequence counter
        # Time - O(n)
        # Space - O(26) - O(1)

        freq = Counter(s)
        remove = 0

        for k, v in freq.items():
            if v % 2:
                remove += (v - 1) # Odd case
            else:
                remove += (v - 2)  # Even case
            
        return len(s) - remove

        
