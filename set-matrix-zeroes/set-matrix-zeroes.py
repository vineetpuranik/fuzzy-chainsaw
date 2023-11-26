import unittest
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # Approach 1
        # Create a copy of the matrix. 
        # Iterate the matrix element by element. If we find a 0 then in the copy of the matrix, update all the elements for the same row and column to 0. 
        # Return the copy. Quadratic time solution. Not efficient. 

        # Approach 2 
        # Create 2 arrays one of size m and other of size n. Initialize them to 1
        # Iterate the matrix element by element. If we find a 0 then in array m update the rth index to 0 and in array n update the cth index to 0. 
        # arrays m, n will now contain the details on which row and which columns in the matrix should be set to 0. 
        # Iterate the matrix again and update. 
        # Space O(m + n). Time O(mn)

        # Approach 3 
        # Instead of creating 2 arrays of size m and n we can use the 1st row and 1st column of the matrix as our markers. 
        # Quick note here is that matrix[0][0] will be common for both the 1st row and 1st column hence, we need to create 2 variables for marking the first row and first col
    


        rows, cols = len(matrix), len(matrix[0])
        zeroRowMarker = False
        zeroColMarker = False

        # Mark the 0th row and 0th column
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r == 0:
                        zeroRowMarker = True
                    if c == 0:
                        zeroColMarker = True
                    if r > 0 and c > 0:
                        matrix[0][c] = 0
                        matrix[r][0] = 0

        # Update the matrix except the first row and first column
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Update the first row if needed
        if zeroRowMarker:
            for c in range(cols):
                matrix[0][c] = 0

        # Update the first column if needed
        if zeroColMarker:
            for r in range(rows):
                matrix[r][0] = 0