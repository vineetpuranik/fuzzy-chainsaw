## Set Matrix zeroes
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

## ALgorithm 
Use the first row and first col as markers for updating the matrix rows and cols to zeroes. 
matrix[0][0] is common element for rows and cols and hence create 2 new vars for 0th row and 0th col. 
This will help us with achieving O(1) space and O(mn) time. 


