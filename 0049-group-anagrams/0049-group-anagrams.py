from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solution 1 - sorting the key with HashMap usage
        # O(m*nlogn) time
        # O(m) space

        # sorting is an nlog(n) operation. your overall solution would take mn*log(n) time where m is the number of words in the array.
        # 
        # d = {}

        # for s in strs:
        #     t = ''.join(sorted(s))

        #     if t in d:
        #         d[t].append(s)
        #     else:
        #         d[t] = [s]

        # return d.values()



        # Solution 2 - improve the solution to O(n) using frequency count through arrays
        # O(m * n * 26) = O(m*n) where m is the number of strs and n is the number of chars in a string
        # O(m) space


        # d = defaultdict(list)

        # for s in strs:
        #     t = [0] * 26
        #     for c in s:
        #         t[ord(c) - ord('a')] += 1
        #     d[tuple(t)].append(s)

        # return d.values()



        # RE-DO for the interview
        # Time for sorting - O(N * Klog(K)) where N is the number of words in strs and 
        #                             K is the maximum length of the string in strs
        # Time for tuple as key - O(N * K), where N is the length of strs and K is the maximum length of a string in strs.
        #
        # Space - O(N * K)


        # from collections import defaultdict

        # d = defaultdict(list)

        # for w in strs:
        #     key = [0]*26
        #     for c in w:
        #         key[ord('a')-ord(c)] += 1
        #     d[tuple(key)].append(w)

        # return d.values()


        # res = []

        # d = defaultdict(list)

        # for w in strs:
        #     key = [0] * 26

        #     for c in w:
        #         key[ord(c)-ord('a')] += 1

        #     d[tuple(key)].append(w)



        # for v in d.values():
        #     res.append(v)

        # return res


        # from collections import defaultdict

        # groups = defaultdict(list)

        # for w in strs:
        #     key = (0, )
        #     groups["".join(sorted(w))].append(w)


        # return [val for val in groups.values()]


        # groups = collections.defaultdict(list)

        # for s in strs:
        #     groups[''.join(sorted(s))].append(s)

        # return groups.values()

        # Time - O(N*K)
        # Space - O(N)

        groups = collections.defaultdict(list)

        for s in strs:
            key = [0] * 26

            for c in s:
                key[ord(c) - ord('a')] += 1

            groups[tuple(key)].append(s)

        return list(groups.values())
