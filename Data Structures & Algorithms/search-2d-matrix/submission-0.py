class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix) # rows
        n = len(matrix[0]) # columns

        lo = 0 
        hi = (m*n) - 1

        while lo <= hi:
            idx = (lo + hi)//2
            row = idx//n  
            col = idx%n # how far along we are

            if matrix[row][col] == target:
                return True 
            
            if matrix[row][col] > target:
                hi = idx - 1
            else:
                lo = idx + 1
        
        return False





        