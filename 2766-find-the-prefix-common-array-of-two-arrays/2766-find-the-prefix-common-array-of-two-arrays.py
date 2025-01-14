class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        # Solution 1 
        # Time - 
        # Space - 


        seen_a, seen_b = set(), set()
        res = []

        for idx in range(len(A)):
            seen_a.add(A[idx])
            seen_b.add(B[idx])
            res.append(len(seen_a.intersection(seen_b)))

        return res