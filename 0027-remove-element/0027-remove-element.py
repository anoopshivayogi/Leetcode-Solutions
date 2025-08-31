class Solution:
    # def removeElement(self, nums: List[int], val: int) -> int:


        # if len(nums) == 1 and nums[0] == val:
        #     return 0

        # n = len(nums)

        # i = n-1
        # j = 0

        # while j < i:

        #     while i >= 0 and nums[i] == val:
        #         i -= 1

        #     while j < n and nums[j] != val:
        #         j += 1

        #     if j >= i:
        #         break

        #     nums[j], nums[i] = nums[i], nums[j]

        # return i+1


    
        # i = 0

        # for j in range(len(nums)):
        #     if nums[j] != val:
        #         nums[i] = nums[j]
        #         i += 1
        
        # return i

    def removeElement(self, arr: List[int], val: int) -> int:

        if len(arr) == 1:
            if arr[0] == val:
                return 0
            else:
                return 1

        count = 0

        l, r = 0, len(arr) - 1
        while l < r:
            while l < len(arr) and arr[l] != val: # You want to delete
                l += 1

            while  r >= 0 and arr[r] == val: # Already deleted side
                r -= 1

            if l >= r:
                break

            arr[l], arr[r] = arr[r], arr[l]

        return r+1


        # [2, 2] ; val = 2
        #  l
        #  r

        # j == l and i == r

        # [2, 2, 3, 3] ; val = 3
        #        l        
        #     r

        # [3, 3] ; val = 5
        #  l
        #     r
