class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visited, prevHeight):
            
            if (r >= 0 and r < ROWS and #check r is in bound
                c >= 0 and c < COLS and # check c is in bound
               (r,c) not in visited and   # check (r, c) is not already visited
               heights[r][c] >= prevHeight) : #check if height of current cell is >= the prev cell which explored this cell
                
               visited.add((r, c)) #add to visited
               dfs(r, c-1, visited, heights[r][c]) #go to adjacent left cell
               dfs(r, c+1, visited, heights[r][c]) # go to adjacent right cell
               dfs(r-1, c, visited, heights[r][c]) # go to adjacent top cell
               dfs(r+1, c, visited, heights[r][c]) # go to adjacent bottom cell
            
            return    
                
        
        

        # start DFS from cells adjacent to pacific and atlantic ocean and then work inwards
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS -1, atlantic, heights[r][COLS - 1])
        
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])
        
        results = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    results.append([r, c])
        
        return results