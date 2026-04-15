class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        

        # Solution 1 - Using hashmap
        # Time - O(n)
        # Space - O(n)

        seen = defaultdict(list)

        for idx, n in enumerate(nums):
            seen[n].append(idx)

        res = 300

        for k, v in seen.items():
            if len(v) >= 3:
                for i in range(len(v)-2):
                    res = min(res, (v[i+1]-v[i]) + (v[i+2]-v[i+1]) + (v[i+2] - v[i]))

        return res if res != 300 else -1