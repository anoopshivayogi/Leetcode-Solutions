from functools import lru_cache

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # cache = {}

        # # @cache
        # def top_down(st):
        #     if st in cache:
        #         return cache[st]
            
        #     if st == '':
        #         return True

        #     for w in wordDict:
        #         if st.startswith(w):
        #             if top_down(st[len(w):]):
        #                 cache[st] = True
        #                 return True

        #     cache[st] = False

        #     return False

        # return top_down(s)
        

        # Best solution
        # def bottom_up(target, wordBank):

        #     table = [False] * (len(target)+1)
        #     table[0] = True

        #     for i in range(len(target)+1):
        #         if table[i]:
        #             for ele in wordBank:
        #                 if target[i:i + len(ele)] == ele:
        #                     table[i+len(ele)] = True

        #         # Extra statements to improve efficiency 
        #         # if table[len(target)]:
        #         #     return True
            
        #     return table[len(target)]

        # return bottom_up(s, wordDict)


        # def bottom_up_approach_2(target, wordBank):
        
        #     table = [False] * (len(target)+1)
        #     table[len(target)] = True

        #     for i in range(len(target)-1, -1, -1):
        #         for w in wordBank:
        #             if i + len(w) <= len(target) and target[i:i+len(w)] == w:
        #                 table[i] = table[i + len(w)]
        #             if table[i]:
        #                 break

        #     return table[0]

        
        # return bottom_up_approach_2(s, wordDict)


        # from functools import cache

        # @cache
        # def dfs(s):
        #     if s == "":
        #         return True 

        #     for w in wordDict:
        #         if s.startswith(w):
        #             if dfs(s[len(w): ]):
        #                 return True

        #     return False

        # return dfs(s)


        # Dynamic programming solution
        # Time - O(n * m); where n is length of s and m as the length of wordDict
        # Space - O(n)

        # n = len(s)
        # dp =  [False] * (n+1)
        # dp[n] = True

        # for i in range(n-1, -1, -1):

        #     for w in wordDict:
        #         if i + len(w) <= n:
        #             if s[i: i+len(w)] == w and dp[i+len(w)]:
        #                 dp[i] = True

        # return dp[0]


        # Re-do for the interview
        # Time - O(n*m*n) = O(n^2*m) reduce it to O(n*m) when memoized
        # Space - (n)

        cache = {}

        def dfs(cur_str):
            if cur_str in cache:
                return cache[cur_str]

            if cur_str == "":
                cache[cur_str] = True
                return True


            for word in wordDict:
                if cur_str.startswith(word):
                    if dfs(cur_str[len(word): ]):
                        cache[cur_str] = True
                        return True

            cache[cur_str] = False
            return False


        return dfs(s)
        

        