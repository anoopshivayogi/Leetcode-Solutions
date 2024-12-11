class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Solution 1 - Recursive 
        
        
        # result = []
        # subsets = []
        
        # def backTrack(i):
        #     if i >= len(nums):
        #         result.append(subsets.copy())
        #         return

        #     subsets.append(nums[i])
        #     backTrack(i+1)

        #     subsets.pop()
        #     backTrack(i+1)

        
        # backTrack(0)

        # return result


        # Solution 2 - Recursive 

        # result = []
        
        # def backTrack(i, subset):
        #     if i >= len(nums):
        #         result.append(subset)
        #         return

        #     subset.append(nums[i])
        #     backTrack(i+1, subset.copy())

        #     subset.pop()
        #     backTrack(i+1, subset.copy())

        
        # backTrack(0, [])

        # return result



        # Solution 3 - Recursive 

        # result = []
        
        # def backTrack(i, subset):
        #     if i >= len(nums):
        #         result.append(subset.copy())
        #         return

        #     subset.append(nums[i])
        #     backTrack(i+1, subset)

        #     subset.pop()
        #     backTrack(i+1, subset)

        
        # backTrack(0, [])

        # return result



        # Finding subsets/subsequence for a string 
        # NOTE : doesn't require stack necessarily to pass as parameter.
        

        # res = []

        # st = "abc"

        # def subsets(i, s):
        #     global st
            
        #     if i == len(st):
        #         res.append(s)
        #         return 
                
        #     # included 
        #     subsets(i + 1, s + st[i])
            
        #     # Not Included 
        #     subsets(i + 1, s)
            

        # subsets(0, '')

        # print(res)




        # Re-do for the interview
        # Time - 
        # Space - 

        # Intuition - 

    #                            ''                

    #               [1]                        []                         0

    #        [1,2]         [1]          [2]            []                 1

    #  [1,2,3]  [2]  [1, 3] [1]. [2, 3].  [3].   [1,3]. []                2

        # path = []
        # res = []

        # def subsets(i):
        #     if i >= len(nums):
        #         res.append(path[:])
        #         return

        #     path.append(nums[i])
        #     subsets(i+1)
        #     path.pop()
        #     subsets(i+1)

        # subsets(0)

        # return res


        # Re-do for the interview 
        # Time - O(n*2^n)
        # Space - O(n)
        res = []
        path = [] # space O(N)

        def dfs(idx):

            if idx >= len(nums): # O(n)
                res.append(path.copy())
                return

            path.append(nums[idx])

            dfs(idx + 1)

            path.pop()

            dfs(idx + 1)

        dfs(0)

        return res






