class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # res = []

        # for i in range(len(intervals)):

        #     if newInterval[1] < intervals[i][0]:
        #         res.append(newInterval)
        #         return res + intervals[i:]
        #     elif newInterval[0] > intervals[i][1]:
        #         res.append(intervals[i])
        #     else:
        #         newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        # res.append(newInterval)

        # return res



        # Re-Do for the interview
        # Time - O(n)
        # Space - O(1)

        # res = []

        # for i in range(len(intervals)):

        #     if intervals[i][1] < newInterval[0]:
        #         res.append(intervals[i])
        #     elif newInterval[1] < intervals[i][0]:
        #         res.append(newInterval)  # I have done the insertion; now time to append rest of the intervals and return
        #         return res + intervals[i:]
        #     else:  # overlapping case
        #         newInterval[0] = min(intervals[i][0], newInterval[0])
        #         newInterval[1] = max(intervals[i][1], newInterval[1])

        # res.append(newInterval)
        # return res


        # Intuition

        # Three cases in total
        # First case: Inserting new interval before all the intervals 
        #     |0 new 5|  |6 10|  |15 20| 

        # Second case: Inserting new interval after all the intervals
        #     |0   5|  |6  10|  |15 20|  |21 new 25| 


        # Third case: Inserting new interval overlapping 
        #     |0  5| |4 new 15| |6 10| |15 20|


        # keep merging new_interval and append only after the overlapping is done
        # |0 15 | - first merge
        # |0 20 | - second merge
        # Finally - |0 20| and return

        res = []


        for i in range(len(intervals)):

            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            
            else: # Overlapping
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        res.append(newInterval)
        
        return res

