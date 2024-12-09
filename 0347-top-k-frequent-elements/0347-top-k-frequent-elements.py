import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution 1 - using heap 
        # time - O(klogn); where k is the input and O(logn) for each pop from heapq; heapify is O(n)
        # space - O(N + k) where N is for storing counter hashmap and k is number of heap elements

        # d = Counter(nums)
        # l = []
        # res = []

        # for key, val in d.items():
        #     l.append((-val, key))
        
        # # Inherently min heap
        # heapq.heapify(l)


        # while k>0:
        #     res.append(heapq.heappop(l)[1])
        #     k -= 1
        
        # return res


        # Solution 2 - using heap but with a bit of twist; the above solution is better
        # time - O(N log k) -> O((N-k) * logk) -> O(N log k) [O(logk) for each push and pop with (N-k) times]
        # space - O(n)

        # n = len(nums)

        # if k == n or n == 1:
        #     return nums

        # minHeap = []
        # res = []
        # freq = {}

        # for i in range(n):
        #     freq[nums[i]] = 1 + freq.get(nums[i], 0)

        # freq = [(v, k) for k, v in freq.items()]

        # i = 0

        # while i < k:
        #     heapq.heappush(minHeap, freq[i])
        #     i += 1

        # while i < len(freq):
        #     heapq.heappush(minHeap, freq[i])
        #     heapq.heappop(minHeap)
        #     i += 1

        # for e in minHeap:
        #     res.append(e[1])

        # return res



        # Solution 2 - using varitation of bucket sort
        # O(n) time complexity 
        # O(m + n) space, given m is freq and n is counter


        # n = len(nums)
        # freq = [[] for i in range(n + 1)]
        # counter = {}
        # res = []

        # for num in nums:
        #     counter[num] = 1 + counter.get(num, 0)


        # for key, val in counter.items():
        #     freq[val].append(key)


        # for i in range(n, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #     if len(res) == k:
        #         break

        # return res



        # Solution 0 - using sorting technique
        # Time - O(nlogn) for sorting
        # Space - O(1) - in case of heapsort implementation


        # freq = Counter(nums)

        # freq = sorted(freq.items(), key=lambda x: x[1])

        # res = []

        # while k:
        #     res.append(freq.pop()[0])
        #     k -= 1

        # return res

        

        # Re-Do for interview
        # Important base case to avoid NlogN time complexity, 
        # if K==len(nums) then time complexity will be NlogN
        # Space - O(N + k)

        # if k == len(nums):
        #     return nums

        # import heapq

        # freq = Counter(nums)
        # res = []

        # maxH = []

        # for key, v in freq.items():
        #     maxH.append((-v, key))

        # heapq.heapify(maxH)

        # while k>0:
        #     print(k)
        #     res.append(heapq.heappop(maxH)[1])
        #     k -= 1


        # return res


        # freq = collections.Counter(nums)

        # buckets = [[] for i in range(len(nums)+1)]
        # res = []

        # for key, val in freq.items():
        #     buckets[val].append(key)

        # for b in buckets[::-1]:
        #     if b and k:
        #         for val in b:
        #             res.append(val)
        #             if len(res) == k:
        #                 return res

        # return res


        # Re-Do for interview
        # Time - O(k * log(n))

        # import heapq

        # freq = collections.Counter(nums)

        # max_heap = []
        # res = []

        # for key, val in freq.items():
        #     max_heap.append((-val, key))

        # heapq.heapify(max_heap)

        # while k > 0:
        #     res.append(heapq.heappop(max_heap)[1])
        #     k -= 1

        # return res


        # Time - O(n)
        # Space - O(n)
        # [1,1,1,2,2,3] -> [[], [3 ], [2 ], [1 ], [], [], []]
        # {1: 3, 2: 2, 3: 1}


        # freq = collections.Counter(nums)
        # res = []

        # buckets = [[] for _ in range(len(nums) + 1)]

        # for key, val in freq.items():
        #     buckets[val].append(key)

        # for i in range(len(buckets) - 1, -1, -1):
        #     for ele in buckets[i]:
        #         res.append(ele)
        #         if len(res) == k:
        #             return res


        # freq = Counter(nums)
        # buckets = [[] for _ in range(len(nums)+1)]

        # for key, val in freq.items():
        #     buckets[val].append(key)

        # res = []

        # for i in range(len(buckets) - 1, -1, -1):
        #     for ele in buckets[i]:
        #         res.append(ele)
        #         if len(res) == k:
        #             return res

        # return []


        # res = []

        # buckets = [[] for _ in range(len(nums) + 1)]
        # freq = collections.Counter(nums)

        # for key, val in freq.items():
        #     buckets[val].append(key)

        # for i in range(len(buckets)-1, -1, -1):
        #     for ele in buckets[i]:
        #         res.append(ele)
        #         if len(res) == k:
        #             return res

        # return []



        # res = []
        # buckets = [[] for _ in range(len(nums) + 1)]

        # freq = collections.Counter(nums)

        # for key, val in freq.items():
        #     buckets[val].append(key)

        # for i in range(len(buckets) - 1, -1, -1):
        #     for ele in buckets[i]:
        #         res.append(ele)

        #         if len(res) == k:
        #             return res
        # return []

        # Solution 3 - Quick Select solution
        # Time - O(n^2) at worst and O(n) on average reduced from  O(n log n)[Quick Sort]
        # Space - O(logn) at best and O(n) at worst

        def partition(arr, l, r):
            i = l
            pivot = arr[r][1]

            for j in range(l, r):
                if arr[j][1] <= pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1

            arr[i], arr[r] = arr[r], arr[i]
            return i # Return pivot's index


        def quick_select(arr, l, r, k):
            pivot_idx = partition(arr, l, r)

            if pivot_idx == k:
                return arr[k:]
            elif pivot_idx > k:
                return quick_select(arr, l, pivot_idx - 1, k)
            else:
                return quick_select(arr, pivot_idx + 1, r, k)


        freq = collections.Counter(nums)
        arr = list(freq.items())
        res = quick_select(arr, 0, len(arr) - 1, len(arr) - k)
        res = [x[0] for x in res]
        return res
