class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        

        # Solution 1 - Kinda brute force using BFS 
        # Time - 
        # Space - 


        seen = set(wordList)
        visit = set([beginWord])
        q = collections.deque()
        q.append((beginWord, 1)) # word, path length

        while q:
            cur_word, path_len = q.popleft()

            if cur_word == endWord:
                return path_len

            for i in range(len(cur_word)):
                for j in range(26):
                    word = cur_word[:i] + chr(ord('a') + j) + cur_word[i+1: ]
                    if word in seen:
                        if word not in visit:
                            visit.add(word)
                            q.append((word, path_len + 1))

        return 0