class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Solution 1 - using ordered hashmap
        # Time - O(n)
        # Space - O(26) which is fixed size = O(1)

        # order = {key: idx for idx, key in enumerate(order)}

        # for i in range(len(words) - 1):
        #     w1, w2 = words[i], words[i + 1]

        #     for j in range(len(w1)):

        #         if len(w2) == j:
        #             return False

        #         if w2[j] != w1[j]:
        #             if order[w2[j]] < order[w1[j]]:
        #                 return False
        #             break

        # return True


        # Re-do for the interview
        # Time - O(M) where M is the total number of characters in the words and O(N) = O(26) for constructing order_idx
        # Space - O(26) = O(1)

        # order_idx = {key: idx for idx, key in enumerate(order)}

        # for i in range(len(words) - 1):

        #     word1 = words[i]
        #     word2 = words[i + 1]

        #     for j in range(len(word1)):

        #         if len(word2) == j: # Second word cannot be a prefix of the 1st
        #             return False

        #         if word1[j] != word2[j]:
        #             if order_idx[word2[j]] < order_idx[word1[j]]:
        #                 return False
        #             break  # Otherwise two words are in correct order; First unmatched and in correct order

        # return True


        # Re-do for the interview - Wihout using hashing
        # Time - O(n)
        # Space - O(26) = O(1)

        # order_dict = {key: idx for idx, key in enumerate(order)}
        order_dict = [0] * 26

        for idx, c in enumerate(order):
            order_dict[ord(c) - ord('a')] = idx

        for i in range(len(words) - 1):

            word1 = words[i]
            word2 = words[i + 1]

            for j in range(len(word1)):

                if len(word2) == j:
                    return False

                if word1[j] != word2[j]:
                    if order_dict[ord(word1[j]) - ord('a')] > order_dict[ord(word2[j]) - ord('a')]:
                        return False
                    break

        return True