class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:

        # Solution 1 - Using hashmap to club all the person with the same age
        # Time - O(n)
        # Space - O(120) = Only 120 different ages possible = O(1)
        # video - https://www.youtube.com/watch?v=0_4H68f85HQ


        def can_friend(x, y):
            if y <= (0.5 * x) + 7:
                return False

            if y > x:
                return False

            return True

        age_frequency = collections.Counter(ages)
        res = 0

        for age_a, freq_a in age_frequency.items():
            for age_b, freq_b in age_frequency.items():

                if can_friend(age_a, age_b):
                    res += (freq_a * freq_b)

                    if age_a == age_b:
                        res -= freq_a

        return res
