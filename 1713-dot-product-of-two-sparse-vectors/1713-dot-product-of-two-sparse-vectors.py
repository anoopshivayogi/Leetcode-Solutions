class SparseVector:
    def __init__(self, nums: List[int]):
        # Solution 0 - Brute Force
        # Time - O(N)
        # Space - O(N)

        # self.nums1 = nums


        # Solution 1 - HashMap solution
        # Time - O(L1 + L2) + O(N) = O(n); L1 and L2 are the non-zero numbers in the array respectively
        # Space - O(L1 + L2)

        # self.nums1 = {}

        # for idx, n in enumerate(nums):
        #     if n != 0:
        #         self.nums1[idx] = n


        # NOTE: Follow-up : What if the hashing isn't efficient and I want to use array instead
        # Solution 3 - Using index-value pairs
        # Time - O(n) + O(L1 + L2) = O(n)
        # Space - O(L1 + L2)

        # self.nums1 = []

        # for idx, n in enumerate(nums):
        #     if n != 0:
        #         self.nums1.append((idx, n))

        # Solution 4 - Follow up: What if only one of the vectors is sparse?
        # Time - O(n * log(n))
        # Space - O(L1 + L2)

        # NOTE: Take the array that is smaller and Do a binary search on the second list; 
        # to find if the particular index exists or not. 

        # Re-do for the interview
        # Solution 1 - using hashmap to store non zero elements
        # Time - O(L1 + L2) where L1 and L2 are non-zero elements in the num1 and nums2
        # Space - O(L1 + L2)
        self.nums = {}

        for idx, num in enumerate(nums):
            self.nums[idx] = num


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        # Solution 0 - Brute Force

        # res = 0

        # for i in range(len(self.nums1)):
        #     res += (self.nums1[i] * vec.nums1[i])

        # return res


        # Solution 1 - Hashmap Solution

        # res = 0

        # for k, v in self.nums1.items():
        #     if k in vec.nums1:
        #         res += v * vec.nums1[k]

        # return res

        # Solution 2 - improvement to HashMap solution

        # res = 0

        # # Determine which dictionary has fewer keys
        # if len(self.nums1) <= len(vec.nums1):
        #     smaller_dict = self.nums1
        #     larger_dict = vec.nums1
        # else:
        #     smaller_dict = vec.nums1
        #     larger_dict = self.nums1

        # # Iterate through the smaller dictionary
        # for k, v in smaller_dict.items():
        #     if k in larger_dict:
        #         res += v * larger_dict[k]

        # return res

        # Solution 3 - Using index-value pairs - If the hash algorithm is bad

        # i, j = 0, 0
        # res = 0

        # while i < len(self.nums1) and j < len(vec.nums1):
        #     i_idx, i_num = self.nums1[i]
        #     j_idx, j_num = vec.nums1[j]

        #     if i_idx == j_idx:
        #         res += (i_num * j_num)
        #         i += 1
        #         j += 1
        #     elif i_idx > j_idx:
        #         j += 1
        #     else:
        #         i += 1

        # return res


        # Re-do for the interview
        # Time - 
        # Space - 

        res = 0

        # Always self.nums will be the smallest
        if len(self.nums) > len(vec.nums):
            self.nums, vec.nums = vec.nums, self.nums

        for k, v in self.nums.items():
            if k in vec.nums:
                res += (v * vec.nums[k])
        
        return res


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
