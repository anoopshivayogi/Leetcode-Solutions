class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        

        # Solution 1 - Using a marker list 
        # let n be the length of the string and m be the length of the words and k be the average length of the word

        # Time - O(n * m * k)
        # Space - O(n)
        # https://www.youtube.com/watch?v=4JPKLcpggCE

        n = len(s)

        flags = [False] * n
        cur_end = 0

        for i in range(n):   # O(n)
            for word in words:  # O(m)
                if s.startswith(word, i):  # NOTE: Learn this usage correctly.  # O(k)
                    cur_end = max(cur_end, i + len(word))

            if i < cur_end:
                flags[i] = True

        res = []

        for i in range(n):

            if flags[i] and (i == 0 or (i > 0 and not flags[i - 1])):
                res.append("<b>")
                
            res.append(s[i])

            if flags[i] and (i == n - 1 or (i < n - 1 and not flags[i + 1])):
                res.append("</b>")

        return "".join(res)


        # At the worst case; k can be n*(n-k) = O(n^2 - n.k)
        # If you have all the s combinations in the words; then it can go n^2 time complexity
        # s = [aaa]; words = ["a", "aa", "aaa"]
