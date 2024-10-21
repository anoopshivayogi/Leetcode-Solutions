class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        # Solution 1 - Using set to see if you've seen a parent folder before
        # Time - 
        # Space - 

        folder.sort()

        seen = set()
        res = []

        for f in folder:
            exist = False
            for idx, ch in enumerate(f):
                if ch == "/":
                    if f[:idx] in seen:
                        exist = True
                        break

            if not exist:
                seen.add(f)

        return list(seen)
