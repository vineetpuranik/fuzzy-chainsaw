## Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.


## Algorithm
1. Initially count all the fresh oranges and add all the rotten oranges to a queue.
2. While there are element in the queue and fresh oranges > 0 run a loop that will run for the number of elements currently in the queue. Usually a for loop on the length of the queue. 
3. Pop left from the queue, This will give us a rotten orange and for that orange mark all the 4 neighbors that are fresh as rotten. Decrement count and add the new rotten to the end of the queue. 
4. Once all the initial rotten oranges are taken care of , increase the minutes and start the loop again.
5. This is an example of multi-node BFS