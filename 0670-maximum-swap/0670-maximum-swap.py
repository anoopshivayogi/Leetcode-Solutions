class Solution:
    def maximumSwap(self, num: int) -> int:

        # Solution 1 - Using two pass -- findings max right and min left 
        # Time - O(N) - where N is the number of digits in the input
        # Space - O(N)

        # Dry-Run

        # num = 2 7 3 6
        # max   7 7 6 6
        # idx   2 2 3 3


        if num <= 11:
            return num

        # Convert number to array of chars
        num_array = [int(x) for x in str(num)]
        # num_array = list(str(num))  # NOTE: This also works well to convert

        # Find Max from the right

        max_seen = float('-inf')
        max_seen_idx = -1

        for i in range(len(num_array) - 1, -1, -1):

            num_array[i] = (num_array[i], max_seen, max_seen_idx)

            if num_array[i][0] > max_seen:
                max_seen = num_array[i][0]
                max_seen_idx = i

        # Find a lower element from left than the max_to_right and that is the swap point

        for i in range(len(num_array)):
            cur_num, max_to_right, max_idx = num_array[i]

            if max_to_right > cur_num:
                num_array[i], num_array[max_idx] = num_array[max_idx], num_array[i]
                break

        # Convert the individual number to a single number and return the result

        num = 0

        for n in num_array:
            num = num * 10 + int(n[0])

        return num


        # Alternative way of string handling
        # num = ''

        # for n in num_array:
        #     num += str(n[0])

        # return int(num)
