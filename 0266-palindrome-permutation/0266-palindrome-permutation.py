class Solution:
    def canPermutePalindrome(self, s: str) -> bool:


        # Solution 1 - Using frequency and making sure only one odd frequency item is present
        # Time - O(2n)
        # Space - O(26) -- Since there are only 26 lowercase characters
        
        # seen_odd = False
        # freq = collections.Counter(s)

        # for k, v in freq.items():

        #     if v % 2 == 1:
        #         if not seen_odd:
        #             seen_odd = True
        #         else:
        #             return False

        # return True



        # Solution 2 - Using set to count odd and evens smartly
        # Time - O(n)
        # Space - O(26)
        
        seen = set()

        for c in s:
            if c not in seen:
                seen.add(c)
            else:
                seen.remove(c)

        return len(seen) <= 1
