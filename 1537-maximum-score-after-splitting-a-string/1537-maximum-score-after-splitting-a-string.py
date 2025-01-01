class Solution:
    def maxScore(self, s: str) -> int:
        
        # Solution 1 - multiple pass
        # Time - O(n)
        # Space - O(1)

        left, right = 0, 0
        res = 0

        for d in s:
            if d == '1':
                right += 1

        for i in range(len(s)-1):
            if s[i] == '0':
                left += 1
            if s[i] == '1':
                right -= 1

            score = left + right

            if score > res:
                res = score

        return res



        