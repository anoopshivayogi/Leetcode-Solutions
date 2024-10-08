class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        # Solution 1 - Using DFS and recursion; Kind of brute force
        # Time - O(N)
        # Space - O(log(N)) - Depends on the maximum value; for 50,000, the maximum number of digits is 5 => O(log(n)) with base 10. As 10^5 is approximately 50,000 ; We can argue that the space is constant given maximum

        # res = []

        # def dfs(num):
        #     if num > n:
        #         return 

        #     res.append(num)

        #     num = num * 10

        #     for i in range(10):
        #         dfs(num + i)

        # for i in range(1, 10):
        #     dfs(i)

        # return res


        # Solution 2 - 
        # Time - 
        # Space - 

        cur = 1
        res = []


        while len(res) < n:
            res.append(cur)

            if cur * 10 <= n:
                cur *= 10
            else:
                while cur == n or cur % 10 == 9:
                    cur = cur // 10
                cur += 1

        return res
