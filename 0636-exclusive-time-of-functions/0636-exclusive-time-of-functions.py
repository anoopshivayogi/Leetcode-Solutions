class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        # Solution 1 - Using stack
        # Time - O(n)
        # Space - O(n)

        # res = [0]  * n
        # prev_start = 0
        # stack = []

        # for log in logs:
        #     func_id, action, timestamp = log.split(":")
        #     func_id = int(func_id)
        #     timestamp = int(timestamp)

        #     if action == "start":
        #         if stack: # Start of another task; so you need to end the previous
        #             res[stack[-1]] += timestamp - prev_start

        #         stack.append(func_id)
        #         prev_start = timestamp
        #     else:
        #         res[stack.pop()] += timestamp - prev_start + 1
        #         prev_start = timestamp + 1

        # return res


        prev_start = 0
        st = []
        res = [0] * n


        for log in logs:
            func_id, action, timestamp = log.split(":")
            func_id = int(func_id)
            timestamp = int(timestamp)

            if action == "start":
                if st:  # Previously any task exists; then we need to end it
                    res[st[-1]] += timestamp - prev_start

                prev_start = timestamp
                st.append(func_id)
            else:

                res[st.pop()] += timestamp - prev_start + 1
                prev_start = timestamp + 1

        return res