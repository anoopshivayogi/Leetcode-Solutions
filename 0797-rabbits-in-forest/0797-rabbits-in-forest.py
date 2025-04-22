class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        # Solution 1 - using hasmap
        # Time - O(n)
        # Space - O(n)

        freq = defaultdict(int)
        res = 0

        for ele in answers:
            if ele == 0:
                res += 1
                continue
            
            freq[ele] += 1
            if freq[ele] == ele + 1:
                res += freq[ele]
                del freq[ele]

        for k in freq:
            res += (k + 1)

        return res



