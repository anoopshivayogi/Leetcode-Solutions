class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        # Solution 1 - Simple set comparision.
        # Time - O(n)
        # Space - O(26)

        broken = set(brokenLetters)
        text = text.split()
        res = len(text)

        for word in text:
            for ch in word:
                if ch in broken:
                    res -= 1
                    break
        return res


