class Solution:
    def reverseWords(self, s: str) -> str:
        
        # Solution 1 - Using built-in Methods
        # Time - O(3n)
        # Space - O(n)

        # return " ".join(s.split()[::-1])
        

        # Solution 2 - Using queue and without using in-built methods
        # Time - O(2n)
        # Space - O(n)

        string_builder = collections.deque()

        left, i = 0, 0

        while i < len(s):  # O(n)

            if s[i] != " ":
                left = i
                word = ''

                i += 1
                
                while i < len(s) and s[i] != " ":
                    i += 1

                string_builder.appendleft(s[left: i])

                i -= 1

            i += 1

        return " ".join(string_builder)  # O(n)
                
