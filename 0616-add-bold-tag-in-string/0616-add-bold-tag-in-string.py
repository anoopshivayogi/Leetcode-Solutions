class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        

        # Solution 1 - Using a marker list 
        # Time - 
        # Space - 
        # https://www.youtube.com/watch?v=4JPKLcpggCE

        n = len(s)

        flags = [False] * n
        cur_end = 0

        for i in range(n):
            for word in words:
                if s.startswith(word, i):
                    cur_end = max(cur_end, i + len(word))

            if i < cur_end:
                flags[i] = True

        
        print(flags)

        res = []

        for i in range(n):

            if flags[i] and (i == 0 or (i > 0 and not flags[i - 1])):
                res.append("<b>")
                
            res.append(s[i])

            if flags[i] and (i == n - 1 or (i < n - 1 and not flags[i + 1])):
                res.append("</b>")

        return "".join(res)
