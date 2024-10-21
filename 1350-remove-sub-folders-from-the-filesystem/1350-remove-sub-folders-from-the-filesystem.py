class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        # Solution 1 - Using sorting and seen 
        # Time - 
        # Space - 

        folder.sort()

        res = [folder[0]]

        for f in folder[1: ]:
            exist = False
            for idx, ch in enumerate(f):
                if ch == "/":
                    if f[:idx] == res[-1]:
                        exist = True
                        break

            if not exist:
                res.append(f)

        return res
