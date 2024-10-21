class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        

        # Solution 1 - Using Hashmap
        # Time - O(n)
        # Space - O(k) -> Only k remainders is possible that will be keys and a single number as value

        # Intuition - 

        # arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9], k = 5
        # mod = [1, 2, 3, 4, 0,  0, 1, 2, 3, 4]

        # 1. If reminder is 0 and it is odd -> False
        # 2. (reminder - k) mod should be in same freq as the reminder to form a pair.

        # Handle negative number module :
        # (num % k + k) % k -> The (num % k) will put the number within the k bracket.
        # Then add k to convert that negative number to positive.
        # You need to mod it again after converting from negative to positive.


        remainder = collections.defaultdict(int)

        for num in arr:
            remainder[(num % k + k) % k] += 1

        for num in arr:
            
            cur_rem = (num % k + k) % k

            if cur_rem == 0:
                if remainder[cur_rem] % 2:  # If the reminder 0 has odd occurences then it is False
                    return False

            elif remainder[k - cur_rem] != remainder[cur_rem]:
                return False

        return True


        # Solution 2 - Sorting and Two pointers 
        # Time - O(nlogn)
        # Space - O(n) for sorting ;In Python, the sort method sorts a list using the Timsort algorithm which is a combination of Merge Sort and Insertion Sort and has O(n) additional space.
        # Space can be constant if we don't account for the sorting space.


        # arr = sorted(arr, key=lambda num: (num % k + k) % k)

        # left, right = 0, len(arr) - 1

        # while left < right:     # Skip all the numbers with zero remainders

        #     if arr[left] % k != 0:
        #         break

        #     if arr[left + 1] % k != 0:
        #         return False

        #     left += 2

        
        # while left < right:

        #     if (arr[left] + arr[right]) % k != 0:
        #         return False

        #     left += 1
        #     right -= 1

        # return True