class Solution:
    def sortVowels(self, s: str) -> str:
        

        # Solution 1 - Bucket sorting/Counting sort
        # Time - O(N)
        # Space - O(1)

        counts = [[] for _ in range(10)]
        res = list(s)
        vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        mapping = {ord('A') - ord(c): i for i, c in enumerate(['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']) }

        for c in res:
            if c in vowels:
                counts[mapping[ord('A') - ord(c)]].append(c)

        print(counts)
        
        j = 0
        for i, c in enumerate(res):
            if c in vowels:
                while not counts[j]:
                    j += 1
                res[i] = counts[j].pop()
        

        return "".join(res)
                
