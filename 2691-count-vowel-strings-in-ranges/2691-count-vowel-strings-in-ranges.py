class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        

        # Solution 1 - Using prefix + suffix sum
        # Time - O(2m + n)
        # Space - O(m)
        
        #  idx     0. 1. 2. 3. 4.
        #         [0, 1, 1, 2, 3]  
        
        #         [3, 3, 2, 1, 0]

        #         total = 4


        # left = [0] * len(words)
        # prefix = 0

        # vowels = {'a', 'e', 'i', 'o', 'u'}

        # for idx in range(len(words)):
        #     left[idx] += prefix

        #     if words[idx] and (words[idx][0] in vowels) and (words[idx][-1] in vowels):
        #         prefix += 1

        # total = prefix

        # right = [0] * len(words)
        # postfix = 0

        # for idx in range(len(words) - 1, -1, -1):
        #     right[idx] += postfix

        #     if words[idx] and (words[idx][0] in vowels) and (words[idx][-1] in vowels):
        #         postfix += 1

        # res = [0] * len(queries)

        # for idx, q in enumerate(queries):
        #     cur_res = total

        #     cur_res -= left[q[0]]
        #     cur_res -= right[q[1]]

        #     res[idx] = cur_res

        # return res

        # Solution 2 - Just using prefix - more optimised with single pass and O(m) instead of O(2m)
        # Time - O(m + n)
        # Space - O(m)

        #  0  1. 2. 3. 4
        # [1, 1, 2, 3, 4]


        prefix = [0] * len(words)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        cur_prefix = 0

        for idx in range(len(words)):
            if words[idx] and (words[idx][0] in vowels) and (words[idx][-1] in vowels):
                cur_prefix += 1

            prefix[idx] = cur_prefix

        print(prefix)

        res = [0] * len(queries)
        for idx, q in enumerate(queries):
            if q[0] == 0:
                print("res")
                res[idx] = prefix[q[1]]
            else:
                print(idx, prefix[q[1]], prefix[q[0]])
                res[idx] = prefix[q[1]] - prefix[q[0] - 1]

        return res
