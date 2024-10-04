class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        # Solution 1 - Using Topologial sorting - Khan's algorithm
        # Time - 
        # Space - 

        #  t -> f
        #  w -> e
        #  r -> t
        #  e -> r

        #  w -> e -> r -> t -> f

        # adj_list = collections.defaultdict(set)
        # in_degree = collections.defaultdict(int)

        # for word in words:
        #     for char in word:
        #         in_degree[char] = 0


        # for i in range(len(words) - 1):
            
        #     word1 = words[i]
        #     word2 = words[i + 1]

        #     for j in range(len(word1)):

        #         if j == len(word2):
        #             return ""
                
        #         if word1[j] != word2[j]:
        #             if word2[j] not in adj_list[word1[j]]:
        #                 adj_list[word1[j]].add(word2[j])
        #                 in_degree[word2[j]] += 1
        #                 break


        # print(adj_list)
        # q = collections.deque()
        # res = []

        # for key, val in in_degree.items():
        #     if val == 0:
        #         q.append(key)

        # while q:
        #     cur = q.popleft()
        #     res.append(cur)

        #     for neigh in adj_list[cur]:
        #         in_degree[neigh] -= 1
        #         if in_degree[neigh] == 0:
        #             q.append(neigh)

        # return "".join(res) if len(res) == len(in_degree) else ""         


        from collections import defaultdict, deque


        # Step 1: Create a graph
        adj_list = defaultdict(set)  # Adjacency list
        in_degree = defaultdict(int)  # In-degree map
        
        # Initialize the in_degree of all characters
        for word in words:
            for char in word:
                in_degree[char] = 0
        
        # Step 2: Build the graph by comparing adjacent words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            # Check for invalid case: If word2 is a prefix of word1, it's invalid.
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            
            for j in range(min_len):
                if word1[j] != word2[j]:
                    # If word1[j] comes before word2[j], add an edge word1[j] -> word2[j]
                    if word2[j] not in adj_list[word1[j]]:
                        adj_list[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break
        
        # Step 3: Perform topological sort using BFS (Kahn's algorithm)
        # Start with all characters that have in-degree 0
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        order = []
        
        while queue:
            char = queue.popleft()
            order.append(char)
            # Decrease the in-degree of neighbors
            for neighbor in adj_list[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If all characters are not in the order, there's a cycle
        if len(order) != len(in_degree):
            return ""
        
        return "".join(order)
