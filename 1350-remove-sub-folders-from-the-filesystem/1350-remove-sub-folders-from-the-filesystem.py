class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        # 1. Assumptions and edge cases 
        # All are valid strings inside with a '/' followed by lowercase chars.
        # Can't have just a '/', should have atleast one slash followed by a lowercase char.
        # /a exits then /a/b/c is a subfolder. -> True even if /a/b does not exit.

        # 2. Offer the two solutions and time complexity

        # 3. Coding (Correctness, reliability & speed)

        # https://www.youtube.com/watch?app=desktop&v=sFv6T_wLS4k

        # Solution 1 - Using sorting and seen 
        # Time - O(nlogn) + O(n * m) where m is the number of characters inside each folder
        # Space - O(n) or O(1) if you do not consider the resultant array.

        # folder.sort()

        # res = [folder[0]]

        # for f in folder[1:]:
        #     exist = False
        #     for idx, ch in enumerate(f):
        #         if ch == "/":
        #             if f[:idx] == res[-1]:
        #                 exist = True
        #                 break

        #     if not exist:
        #         res.append(f)

        # return res

        # Solution 2 - Trie Solution
        # Time - O(n * m)
        # Space - O()

        class TrieNode:

            def __init__(self, is_folder=False):
                self.is_folder = is_folder
                self.children = {}

        class Trie:

            def __init__(self):
                self.root = TrieNode()

            def insert_folder(self, folder_path):
                cur = self.root

                folders = folder_path.split("/")

                for folder in folders:
                    if folder in cur.children:
                        cur = cur.children[folder]
                    else:
                        cur.children[folder] = TrieNode()
                        cur = cur.children[folder]

                cur.is_folder = True

            def is_sub_folder(self, folder_path):
                cur = self.root

                folders = folder_path.split("/")

                for folder in folders:
                    if cur.is_folder:
                        return True
                    cur = cur.children[folder]

                return False

        trie = Trie()

        for f in folder:
            trie.insert_folder(f)

        res = []

        for f in folder:
            if trie.is_sub_folder(f):
                continue

            res.append(f)

        return res