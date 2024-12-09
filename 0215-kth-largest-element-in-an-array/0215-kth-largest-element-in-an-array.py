class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Solution 0 - Sorting

        # nums.sort()
        # return nums[len(nums)-k]


        # Solution 1 - using heapq
        # time O(n) - for large N. Heapify runs in O(n), but popping k times is O(logN) 
        # final time complexity - O(K LogN)
        # Space - O(n)

        # import heapq

        # for i in range(len(nums)):
        #     nums[i] *= -1

        # heapq.heapify(nums)

        # if k == 1:
        #     return heapq.heappop(nums) * -1

        # for i in range(k-1):
        #     heapq.heappop(nums)

        # return heapq.heappop(nums) * -1


        # solution 2 - QuickSelect - Quicksort style
        # Time - O(n) on an average case - O(n^2) on worst case
        # Space - O(n) 

        # def partition(l, r, arr):
        #     pivot = arr[r]
        #     i = l

        #     for j in range(l, r):
        #         if arr[j] <= pivot:
        #             arr[i], arr[j] = arr[j], arr[i]
        #             i += 1

        #     arr[r], arr[i] = arr[i], arr[r]

        #     return i


        # def quick_select(l, r, arr, k):

        #     pivot = partition(l, r, arr)

        #     if pivot == k:
        #         return arr[pivot]
        #     elif pivot > k:
        #         return quick_select(l, pivot - 1, arr, k)
        #     else:
        #         return quick_select(pivot + 1, r, arr, k)

        # return quick_select(0, len(nums) - 1, nums, len(nums) - k)



        # Solution 3 - 1) With each number, insert it to a minheap;  if the size is over K, remove the minimal (aka. "pop").
        # Exactly this! We can limit the capacity of the heap by K, in the end it will not be O(K LogN) but O(N LogK), which for large N and small K will be very close to O(N).
        # space - O(k)


        # import heapq

        # minHeap = []

        # for num in nums:
        #     heapq.heappush(minHeap, num)
        #     if len(minHeap) > k:
        #         heapq.heappop(minHeap)


        # # return heapq.heappop(minHeap)
        # return minHeap[0]


        # Re-do for the interview


        # NOTE: first edge condition to check
        # Will the k value be less than than the length of the nums ?
        # if it is not; what value should i be returning ? does -1 work ?

        # Time - O(k * logn)
        # Space - O(n)

        for idx in range(len(nums)):
            nums[idx] *= -1

        heapq.heapify(nums)

        k -= 1

        while k:
            heapq.heappop(nums)
            k -= 1

        return -heapq.heappop(nums)

        
        # Time - O(n * logk)
        # [1, 2, 3, 4, 5]; k = 2
        # res = 4

        # min_heap = [5, 4]

        # Re-do for the interview Quick sort solution 
        # Time - O(n) reduced from O(nlogn) in the best case because n + n/2 + n/4 + n/8 = (2n -1)
        # worst case it'll be O(n^2) because n + (n-1) + (n-2) = (n^2)
        # Space - O(logn) in average and O(n) in worst


        # def partition(l, r): # O(n)
        #     pivot = nums[r]
        #     i = l

        #     for j in range(l, r):
        #         if nums[j] <= pivot:
        #             nums[i], nums[j] = nums[j], nums[i]
        #             i += 1
            
        #     nums[r], nums[i] = nums[i], nums[r]

        #     return i


        # def quick_sort(l, r, k):  # logn

        #     pivot = partition(l, r)

        #     if pivot == k:
        #         return nums[pivot]

        #     elif pivot > k:
        #         return quick_sort(l, pivot - 1, k)

        #     else:
        #         return quick_sort(pivot + 1, r, k)

        # return quick_sort(0, len(nums) - 1, len(nums) - k)

        # https://stackoverflow.com/questions/56940793/quickselect-time-complexity-explained



