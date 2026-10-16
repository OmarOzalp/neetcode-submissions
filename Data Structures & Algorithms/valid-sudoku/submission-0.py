class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # each row must contain digits 1-9 no duplicates.
        # column 1/9 no duplicates
        # each of nine suboxes contain a grid must contain digits 1-9
        # no duplicates.. 
        
        # imagine a 2x2

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                g_val = ((row // 3) * 3) + (col//3)
                if val == '.':
                    continue

                if val in rows[row] or val in cols[col] or val in grid[g_val]:
                    return False
                
                grid[g_val].add(val)
                rows[row].add(val)
                cols[col].add(val)
        
        return True
        