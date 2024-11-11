class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        

        # Solution 1 - Using counter for each row, col and diagnoals
        # Time - 
        # Space - 

        n = 3

        rows, cols = [0] * n, [0] * n
        diagonal, anti_diagonal = 0, 0

        player = 1

        for r, c in moves:
            rows[r] += player
            cols[c] += player
            
            if r == c:
                diagonal += player

            if r + c == (n - 1):
                anti_diagonal += player

            if abs(rows[r]) == n or abs(cols[c]) == n or abs(diagonal) == n or abs(anti_diagonal) == n:
                if player >= 0:
                    return "A"
                else:
                    return "B"

            player *= -1
        
        if len(moves) == n * n:
            return "Draw"
        else:
            return "Pending"
