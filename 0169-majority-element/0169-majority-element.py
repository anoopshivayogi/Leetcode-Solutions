class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Solution 1 - hashmap with frequence
        # Time - o(n)
        # Space - o(n)

        # n = len(nums)
        # f = Counter(nums)
        # threshold = floor(n // 2)
        # res = None

        # for k, v in f.items():
        #     if v > threshold:
        #         res = k

        # return res



        # Solution 2 - Boyer moore's majority algorithm 
        # Time - O(n)
        # Space - O(1)

        # cand, count = None, 0

        # for n in nums:
        #     if cand == n:
        #         count += 1
        #     elif count == 0:
        #         cand = n
        #         count += 1
        #     else:
        #         count -= 1

        # return cand



        # Re-Do for interview practise 
        # Time - O(n)
        # Space - O(n)

        # from collections import Counter

        # freq = Counter(nums)
        # threshold = len(nums) / 2

        # for k, v in freq.items():

        #     if v > threshold:
        #         return k 

        # return -1


        # Time - O(n) 
        # space - O(1)

        # cand, count = None, 0

        # for n in nums:

        #     if n == cand:
        #         count += 1
        #     elif count == 0:
        #         cand = n
        #         count += 1
        #     else:
        #         count -= 1

        # return cand


        # major_ele = None
        # count = 0

        # for n in nums: 

        #     if not major_ele or major_ele == n:
        #         major_ele = n 
        #         count += 1
        #     else:
        #         count -= 1
        #         if count == 0:
        #             major_ele = n
        #             count += 1 


        # return major_ele


        majority_ele = None
        count = 0

        for num in nums:
            if not majority_ele or majority_ele == num:
                majority_ele = num
                count += 1
            else:
                count -= 1

                if count == 0:
                    majority_ele = num
                    count = 1

        return majority_ele

        # Tracing

        # nums = [3, 2, 3]
        #               i

        # count = 1
        # majority_ele = 3


        # nums = [2, 2, 1, 1, 1, 2, 2]
        #                           i

        # majority_ele = 2
        # count = 0

     