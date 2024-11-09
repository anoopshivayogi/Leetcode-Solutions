class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        

        seen_odd = False
        freq = collections.Counter(s)

        for k, v in freq.items():

            if v % 2 == 1:
                if not seen_odd:
                    seen_odd = True
                else:
                    return False

            
        return True