class Solution:
    def compressedString(self, word: str) -> str:
        

        # Solution 1 - Using single pointer
        # Time - 
        # Space - 

        cur_char = word[0]
        count = 1
        res = []

        for ch in word[1:]:
            if ch == cur_char and count < 9:
                count += 1
            else:
                count = count % 10
                res.append(str(count) + cur_char)
                count = 1
                cur_char = ch

        res.append(str(count) + cur_char)

        return "".join(res)