class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        # Intuition
        # [0,  0, 1, 0, 1, 1]
        # [11, 8, 5, 4, 3, 4]
        

        # Solution 1 - Prefix and suffix sum
        # Time - O(n)
        # Space - O(1) - the result array is not accounted

        res = [0] * len(boxes)
        prefix_sum = 0
        inc = 0

        for idx in range(len(boxes)):
            res[idx] += prefix_sum

            if boxes[idx] == "1":
                inc += 1

            prefix_sum += inc

        postfix_sum = 0
        inc = 0

        for idx in range(len(boxes) - 1, -1, -1):
            res[idx] += postfix_sum

            if boxes[idx] == "1":
                inc += 1

            postfix_sum += inc

        return res