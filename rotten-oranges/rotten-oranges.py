class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # This is a multi-node BFS problem
        # There will always be 1 row in the grid
        
        #  Possible outputs
        # -1 if there are fresh oranges left after our iteration
        #  0 if there are no fresh oranges at minute 0
        #  x indicating the min number of mins elapsed until no cell has a fresh orange
        
        # rows and cols of the grid
        rows, cols = len(grid), len(grid[0])
        
        # count of fresh oranges
        fresh_oranges = 0 
        
        # minutes elapsed
        minutes = 0
        
        # rotten oranges will be added to a queue
        q = deque()
        
        # iterate over all the cells to get the count of fresh oranges and position of the rotten oranges in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    q.append([r, c])
        
      
        
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            
        # we loop while there are rotten oranges to be processed 
        # additionally we should also check that fresh_oranages > 0
        while q and fresh_oranges > 0 : 
            
            # here len(q) will be length of the queue at the start. 
            # Any new additions to the queue will not alter its length
            for i in range(len(q)):
                # pop the rotten orange from queue
                r, c  = q.popleft()
            
                # check all the 4 adjacent numbers current
                for dr, dc in directions:
                    row = r + dr 
                    col = c + dc

                    # should be in bounds
                    if (row >= 0 and row < len(grid)) and (col >= 0 and col < len(grid[0])):
                        # if fresh make it rotten
                        # decrease the fresh counter
                        # add this rotten orange to our queue
                        if grid[row][col] == 1:
                            grid[row][col] = 2
                            fresh_oranges -= 1
                            q.append([row, col])
                        else:
                            continue
            
            minutes += 1
            
        
        if fresh_oranges == 0:
            return minutes
        else:
            return -1
        
        
        
        
        
        