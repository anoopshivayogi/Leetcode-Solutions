class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        # Solution 1 - Using extra space approach
        # Time - O(n^2)
        # Space - O(n^2)

        # ROWS = len(nums)

        # groups = collections.defaultdict(list)

        # for r in range(ROWS - 1, -1, -1):
        #     for c in range(len(nums[r])):
        #         groups[r + c].append(nums[r][c])

        # res = []
        # idx = 0

        # while idx in groups:
        #     res.extend(groups[idx])
        #     idx += 1

        # return res



        # Solution 2 - Using BFS
        # Time - O(n^2)
        # Space - O(sqrt(n^2))
        # https://www.youtube.com/watch?app=desktop&v=5hG2nDEiwlE


        ROWS = len(nums)
        res = []

        def bfs(r, c):

            q = collections.deque()
            q.append((r, c))

            while q:
                cur_r, cur_c = q.popleft()

                res.append(nums[cur_r][cur_c])

                # Move down
                if cur_c == 0 and cur_r + 1 < ROWS:   # NOTE: TAKE NOT OF THIS cur_c == 0
                    q.append((cur_r + 1, cur_c))

                # Move right
                if cur_c + 1 < len(nums[cur_r]):
                    q.append((cur_r, cur_c + 1))

        bfs(0, 0)

        return res
