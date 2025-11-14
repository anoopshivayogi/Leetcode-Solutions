class Solution:
    def expand(self, s: str) -> List[str]:
        

        # Solution 1 - backtracking/dfs recursive
        # Time - O(3^n or 2^n)
        # Space - O(n)

        inp = []
        idx = 0
        while idx < len(s):
            cur = s[idx]
            if ord(cur) >= ord('a') and ord(cur) <= ord('z'):
                inp.append(cur)
            elif cur == '{':
                inner = []
                while cur != '}':
                    idx += 1
                    cur = s[idx]
                    if cur not in {'}', ','}:
                        inner.append(cur)
                inner.sort()
                inp.append(inner)
            idx += 1

        res = []

        def dfs(idx, cur):
            if idx == len(inp):
                res.append(cur)
                return

            for ch in inp[idx]:
                dfs(idx + 1, cur + ch)

        dfs(0, '')

        return res