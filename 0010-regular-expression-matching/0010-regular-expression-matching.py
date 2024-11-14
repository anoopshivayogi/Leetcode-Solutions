class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        from functools import cache

        @cache
        def dfs(i, j):
            if j >= len(p) and i < len(s):
                return False
            
            if i >= len(s) and  j >= len(p):
                return True

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if (j + 1) < len(p) and p[j + 1] == "*":
                return (match and dfs(i + 1, j)) or dfs(i, j + 2)
                    
            if match:
                return dfs(i + 1, j + 1)

            return False

        return dfs(0, 0)