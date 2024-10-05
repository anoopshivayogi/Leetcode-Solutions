class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        # Solution 1 - Using Topologial sorting - Khan's algorithm
        # let V be the unique letters in the word and E be the edges
        # Time - O(Word * max_word_length + V + E)
        # Space - O(V + E) -> BFS with a queue space complexity and to store all the vertices and edges 

        #  t -> f
        #  w -> e
        #  r -> t
        #  e -> r

        #  w -> e -> r -> t -> f

        adj_list = collections.defaultdict(set)
        in_degree = collections.defaultdict(int)

        for word in words:  # NOTE: One more important step
            for char in word:
                in_degree[char] = 0

        for i in range(len(words) - 1): # O(c)
            
            word1 = words[i]
            word2 = words[i + 1]

            for j in range(len(word1)):

                if j == len(word2):
                    return ""
                
                if word1[j] != word2[j]:
                    if word2[j] not in adj_list[word1[j]]:  # NOTE: 2nd most important thing
                        adj_list[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break  # NOTE: Important to keep this inside first if condition

        q = collections.deque()
        res = []

        for key, val in in_degree.items():
            if val == 0:
                q.append(key)

        while q:
            cur = q.popleft()
            res.append(cur)

            for neigh in adj_list[cur]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    q.append(neigh)

        return "".join(res) if len(res) == len(in_degree) else ""         
