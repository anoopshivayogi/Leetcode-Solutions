from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1 - using inbuilt dicts and comparing frequency
        # O(m) time
        # O(m) space

        # counter1 = Counter(s)
        # counter2 = Counter(t)

        # return counter1 == counter2


        # Solution 2 - using manual dicts and comparing frequency manually
        # O(m * 26) = O(m) time
        # O(26) space, the space remains constant irrespective of input size

        # if len(s) != len(t):
        #     return False

        # dict1 = {}
        # dict2 = {}

        # for i in range(len(s)):
        #     dict1[s[i]] = 1 + dict1.get(s[i], 0)
        #     dict2[t[i]] = 1 + dict2.get(t[i], 0)


        # for k,v in dict1.items():
        #     if k in dict2 and dict2[k] == dict1[k]:
        #         continue
        #     else:
        #         return False

        # return True


        # Solution 3 - using arrays instead of dict
        # O(m * 26) = O(m) time 
        # O(1) space 

        # if len(s) != len(t):
        #     return False

        # arr1 = [0] * 26
        # arr2 = [0] * 26

        # for i in range(len(s)):
        #     arr1[ord(s[i]) - ord('a')] += 1
        #     arr2[ord(t[i]) - ord('a')] += 1

        # return arr1 == arr2



        # Solution 4[Non Efficient time] - using sorting
        # O(mlogn) time
        # O(1) space


        # return sorted(s) == sorted(t)



        # if len(s) != len(t):
        #     return False

        # from collections import defaultdict

        # d_s, d_t = defaultdict(int), defaultdict(int)

        # for i in range(len(s)):
        #     d_s[s[i]] += 1
        #     d_t[t[i]] += 1


        # for k, v in d_s.items():
        #     if k in d_t and d_t[k] == v:
        #         continue
        #     else:
        #         return False

        # return True


        # if len(s) != len(t):
        #     return False


        # from collections import defaultdict

        # s_freq, t_freq = {}, {}

        # for c in s:
        #     if c in s_freq:
        #         s_freq[c] += 1
        #     else:
        #         s_freq[c] = 0

        # for c in t:
        #     if c in t_freq:
        #         t_freq[c] += 1
        #     else:
        #         t_freq[c] = 0

        # for k, v in s_freq.items():
        #     if k in t_freq and t_freq[k] == v:
        #         continue
        #     return False

        # return True


        # Erase

        s_dict, t_dict = {}, {}

        for c in s:
            s_dict[c] = s_dict.get(c, 0) + 1
        
        for c in t:
            t_dict[c] = t_dict.get(c, 0) + 1

        for k, v in s_dict.items():
            if k in t_dict and t_dict[k] == v:
                continue
            
            return False


        for k, v in t_dict.items():
            if k in s_dict and s_dict[k] == v:
                continue

            return False

        return True