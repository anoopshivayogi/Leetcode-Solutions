class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        # Solution 1 - Simple set comparision.
        # Time - O(n)
        # Space - O(26)

        broken = set(brokenLetters)
        text = text.split()
        res = 0

        for word in text:
            broken_flag = False
            for ch in word:
                if ch in broken:
                    broken_flag = True
                    continue
            if not broken_flag:
                res += 1

        return res


