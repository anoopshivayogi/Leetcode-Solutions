class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Solution 1 - Bucket sort   
        # Time - O(n)
        # Space - O(n)

        from collections import Counter

        n = len(nums)
        freq_lst = [0] * (n+1)

        freq = Counter(nums) 

        for k, v in freq.items():
            freq_lst[v] += 1

        for idx in range(n, -1, -1):
            if freq_lst[idx] > 0:
                return freq_lst[idx]*idx


        # from collections import Counter, defaultdict

        # n = len(nums)
        # freq_lst = [0] * (n+1)
        # max_freq = float('inf')

        # freq = defaultdict(int)

        # for n in nums:
        #     freq[n] += 1
        #     max_freq = max(freq[n], max)

        # for k, v in freq.items():
        #     freq_lst[v] += 1

        # print(freq_lst)

        # for idx in range(n, -1, -1):
        #     if freq_lst[idx] > 0:
        #         return freq_lst[idx]*idx

        
