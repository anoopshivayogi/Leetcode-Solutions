class Solution:

    def __init__(self, w: List[int]):
        # self.prefix = []
        # self.w = w
        # cur = 0
        # for ele in w:
        #     cur += ele
        #     self.prefix.append(cur)
        # self.total_sum = cur

        # Re-do for the interview
        # Time - 
        # Space - 

        self.prefix = []
        self.total = 0

        for ele in w:
            self.total += ele
            self.prefix.append(self.total)

        

    def pickIndex(self) -> int:
        # Edge cases callouts - 
        # 1) If the w[i] has all positive integers

        # Intuition - 

        # 1, 2, 3 -> 6

        # 1, 3, 6

        # 1 | 2-3 | 4-6

        # 0 |  1  |  2

        # Solution 1 - Prefix sum and finding a offset to fit in the Prefix sum list where ascending order is not ruined
        # Time - O(n)
        # Space - O(n)

        # import random

        # offset = random.choice(range(1, self.total_sum+1))

        # for i, pre in enumerate(self.prefix):

        #     if offset <= pre:
        #         return i


        # Solution 2 - Binary search to find a place for the offset 
        # Time - O(logn); where n is the number of elements in the w
        # Space - O(1)

        # import random

        # # offset = random.choice(range(1, self.total_sum+1))
        # offset = random.random() * self.total_sum

        # l, r = 0, len(self.prefix)-1

        # # from bisect import bisect_left
        # # pos = bisect_left(self.prefix, offset, l, r) # inbuilt binary search
        # # return pos

        # while l <= r:
        #     mid = (l+r) // 2
        #     if offset <= self.prefix[mid]:
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        # return l


        # def binary_search(arr, offset):
        #     l, r = 0, len(arr)-1

        #     while l <= r:
        #         mid = (l+r) // 2
        #         if offset <= self.prefix[mid]:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        #     return l


        # import random

        # count = 0
        # prefix_sum = []

        # for idx, weight in enumerate(self.w):
        #     count += weight
        #     prefix_sum.append(count)

        # random = random.choice(range(1, count+1))

        # # from bisect import bisect_left

        # idx = binary_search(self.w, random)

        # # idx = bisect_left(prefix_sum, random)

        # return idx

        # # for idx, p in enumerate(prefix_sum):
        # #     if random <= p:
        # #         return idx





        # Re-do for the interview.
        # Time - O(logn)
        # Space - O(1)

        # Intuition
        # [1, 2, 4]
        #  1  3  7

        # 1   |  2-3  |  4-7
        # 1/7 |  2/7  |  4/7


        # def bisect_left(arr, target):
        #     l, r = 0, len(arr) - 1

        #     while l <= r:
        #         mid = (l + r) // 2

        #         # if arr[mid] == target:
        #         #     return mid
        #         if arr[mid] < target:
        #             l = mid + 1
        #         else:
        #             r = mid - 1

        #     return l



        # import random

        # target = random.choice(range(1, self.total_sum + 1))


        # # import bisect

        # # return bisect.bisect_left(self.prefix, target)

        # return bisect_left(self.prefix, target)




        # Re-do for the interview - 2nd Time
        # Let N be the total after adding all the numbers in the array
        # Time - O(logN) - pickIndex has logarithimic but __init__ has O(N)
        # Space - O(1) - pickIndex() has constant time but __init__ has O(N)


        def left_bisect(arr, target):
            l, r = 0, len(arr) - 1

            while l <= r:

                mid = (l + r) // 2
                if arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1  # Last move will be r; so we will select the l instead as our correct answer

            return l
        

        import bisect
        import random

        index = random.choice(range(1, self.total + 1))

        return left_bisect(self.prefix, index)





# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()