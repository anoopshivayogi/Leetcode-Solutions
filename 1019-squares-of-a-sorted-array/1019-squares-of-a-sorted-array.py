class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Solution 0 - using sort function
        # Time - O(nlogn)
        # Space - O(n) - TimSort or log(n) in Java

        # return sorted(i**2 for i in nums) # Generator -> most efficient

        # Solution 1 - using two pointers 
        # Time - O(n)  
        # Space - O(n)


        n = len(nums)
        res = [0]*n

        l, r = 0, n-1 
        idx = n-1

        while l <= r:
            n1 = (nums[l]**2)
            n2 = (nums[r]**2)

            if n1 > n2:
                res[idx] = n1 
                idx -= 1
                l += 1
            else:
                res[idx] = n2 
                idx -= 1 
                r -= 1

        return res