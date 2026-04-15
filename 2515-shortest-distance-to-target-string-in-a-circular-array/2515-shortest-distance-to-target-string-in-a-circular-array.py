class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        

        # Solution 1 - Using two pointers
        # Time - O(n)
        # Space - O(1)


        delta = 0
        n = len(words)

        while delta != n:
            if words[(startIndex + delta) % n] == target:
                return delta
            elif words[(startIndex - delta + n) % n] == target:
                return delta

            delta += 1

        return -1