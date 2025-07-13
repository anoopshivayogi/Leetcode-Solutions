class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:


        # Solution 1 - Sorting + two pointers
        # Time - O(nlogn) + O(mlogm)
        # Space - O(n) - Timsort in python uses O(N) space to sort. 


        players.sort()
        trainers.sort()

        res = 0
        p, t = 0, 0

        while p < len(players):

            if t >= len(trainers):
                break

            if players[p] <= trainers[t]:
                p += 1
                res += 1
            
            t += 1

        return res
