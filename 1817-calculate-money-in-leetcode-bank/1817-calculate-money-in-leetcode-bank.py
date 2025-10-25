class Solution:
    def totalMoney(self, n: int) -> int:
        
        # Solution 1 - Brute force
        # Time - 
        # Space - 

        # func(n) = func(n - 7) + 1

        total = 0
        for day in range(n):
            week = day // 7      # which week (0-indexed)
            day_of_week = day % 7  # which day of the week (0-indexed)
            total += week + day_of_week + 1
        return total