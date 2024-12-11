class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        # Solution 1 - Union find to graph solution 
        # N = number of accounts and K is the maximum length 
        # Time - O(N*Klog(N*K)) - inverse Ackermann function due to path compression
        # Space - O(N*K) + O(N) - sorting space is O(N)

        class UnionFind:

            def __init__(self, n):
                self.parents = [i for i in range(n)]
                self.ranks = [1] * n

            def find(self, node):
                while self.parents[node] != node:
                    node = self.parents[node]
                    self.parents[node] = self.parents[self.parents[node]]  # Compression step 

                return node

            def union(self, n1, n2):

                n1 = self.find(n1)
                n2 = self.find(n2)

                if n1 == n2:
                    return False
                else:

                    if self.ranks[n1] >= self.ranks[n2]:
                        self.parents[n2] = n1
                        self.ranks[n1] += 1
                    else:
                        self.parents[n1] = n2
                        self.ranks[n2] += 1

                return True

        
        uf = UnionFind(len(accounts))

        email_to_idx = {}  # Email -> index in account

        for idx, account in enumerate(accounts):
            for email in account[1:]:  # Exclude the first index
                if email in email_to_idx:
                    uf.union(idx, email_to_idx[email])
                else:
                    email_to_idx[email] = idx

        groups = collections.defaultdict(list)

        for email, idx in email_to_idx.items():
            leader_idx = uf.find(idx)
            groups[leader_idx].append(email)

        res = []

        for idx, emails_lst in groups.items():
            name = accounts[idx][0]
            res.append([name] + sorted(emails_lst))

        return res