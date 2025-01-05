class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        # Solution 1 - Using two pointers + Hashset(to avoid duplicates)
        # Time - O(n*26)
        # Space - O(26^2) = O(1)

        left, right = set(), Counter(s)
        res = set() # Space - O(26^2) - Two spots to fill in the three char palindrome : _ _ _

        for c in s:  # O(n)
            right[c] -= 1
            if right[c] == 0:
                del right[c]

            for j in range(26):  # O(26)
                cur_char = chr(ord('a') + j)
                if (cur_char in left) and (cur_char in right):
                    res.add(cur_char + c + cur_char)
                
            left.add(c)
 
        return len(res)