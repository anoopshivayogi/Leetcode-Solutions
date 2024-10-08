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


        # Solution 2 - Without using recursion
        # Time - O(n)
        # Space - O(1)

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


        # Dry-Run 

        # n = 13

        # cur = 9 ; length = 13
        # res = [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]



        # n = 23

        # cur = 1 ; length = 23
        # res = [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 21, 22, 23, 3, 4, 5, 6, 7, 8, 9, 10]