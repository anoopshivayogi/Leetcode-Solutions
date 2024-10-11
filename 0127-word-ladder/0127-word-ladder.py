class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        

        # Solution 1 - Kinda brute force using BFS 
        # Time - O(n * m^2 * 26)
        # Space - O(n * m^2 * 26)

        # seen = set(wordList)
        # visit = set([beginWord])
        # q = collections.deque()
        # q.append((beginWord, 1)) # word, path_length

        # while q:
        #     cur_word, path_len = q.popleft()

        #     if cur_word == endWord:
        #         return path_len

        #     for i in range(len(cur_word)):   
        #         for j in range(26):
        #             word = cur_word[:i] + chr(ord('a') + j) + cur_word[i+1: ]
        #             if word in seen:
        #                 if word not in visit:
        #                     visit.add(word)
        #                     q.append((word, path_len + 1))

        # return 0


        # Solution 2 - Optimised using patterns
        # N is the number of words and m is the number of characters in the word
        # Time - O(n * m^2)
        # Space - O(n * m^2)

        # NOTE: Edge case

        if endWord == beginWord or not wordList or endWord not in wordList:
            return 0

        adj_lst = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:  # Time: n * m^2; space: same as time
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj_lst[pattern].append(word)

        visit = set([beginWord])
        q = collections.deque([(beginWord, 1)])

        while q:   # Time: n * m ^ 2 ; Space : same as time
            cur_word, length = q.popleft()

            if cur_word == endWord:
                return length

            for i in range(len(cur_word)):
                pattern = cur_word[:i] + "*" + cur_word[i+1:]
                for neigh in adj_lst[pattern]:
                    if neigh not in visit:
                        visit.add(neigh)
                        q.append((neigh, length + 1))
        return 0


        # Solution 3 - Changed question : 
        # use isEnglishWord() method to determine the neighbor instead of the wordList.

        # Time - O(n * m^2 * 26)
        # Space - O(n * m^2 * 26)

        # visit = set([beginWord])
        # q = collections.deque()
        # q.append((beginWord, 1)) # word, path_length

        # while q:
        #     cur_word, path_len = q.popleft()

        #     if cur_word == endWord:
        #         return path_len

        #     for i in range(len(cur_word)):   
        #         for j in range(26):
        #             word = cur_word[:i] + chr(ord('a') + j) + cur_word[i+1: ]
        #             if word.isEnglishWord():
        #                 if word not in visit:
        #                     visit.add(word)
        #                     q.append((word, path_len + 1))

        # return 0
