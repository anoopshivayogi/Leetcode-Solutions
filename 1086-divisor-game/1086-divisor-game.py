class Solution:
    def divisorGame(self, n: int) -> bool:

        # Solution 1 - Most optimized; A game between even and odd
        # Time - O(1)
        # Space - O(1)

        # Intuition - 
        # Understand that for someone to lose the game; they have to be ending up with n == 1 (odd)
        # Since Alice has the first change and she starts the game with even; she can always make it odd for bob by chosing 1
        # If alice always ends up with even and bob odd then bob will end up with 1 and lose the game.
        # The reverse is also true; if alice ends up with odd; then bob can make it odd for alice every time by chosing 1.

        return n % 2 == 0


        # Solution 2 - Dynamic programming
        # Time - 
        # Space - 

