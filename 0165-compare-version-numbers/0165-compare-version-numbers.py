class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        # Solution 1 - Using normal comparision
        # Let N be the number of individual digits separated by .
        # Time - O(2N) - Once to split the individual digits into an array and then to go over the array
        # Space - O(N)
        
        version1 = version1.split(".")
        version2 = version2.split(".")

        p1, p2 = 0, 0

        while p1 < len(version1) or p2 < len(version2):
            val1 = version1[p1] if p1 < len(version1) else 0
            val2 = version2[p2] if p2 < len(version2) else 0
            
            if int(val1) < int(val2):
                return -1
            elif int(val1) > int(val2):
                return 1

            p1 += 1
            p2 += 1

        return 0