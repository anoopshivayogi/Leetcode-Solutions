class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        

        # Solution 0 - Brute force
        # Time - O(N^2)
        # Space - O(1)

        if len(s) != len(goal):
            return False

        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True

        return False