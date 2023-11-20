import unittest
from typing import List, collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # input grid is valid
        if not grid:
            return 0

        # num of rows and cols in the grid
        rows, cols = len(grid), len(grid[0])
        # variable to return the number of islands
        islands = 0
        #set to store the visisted elements in the grid
        visit = set()

        def bfs(r, c):
            # construct queue
            q = collections.deque()
            
            # mark the current grid element as visited.
            visit.add((r, c))
            q.append((r, c))

            #continue exploring while there are elements in the queue
            while q: 
                row, col = q.popleft()
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

                # for explore every neighbor that horizontally adjacent or vertically adjacent
                for dr, dc in directions:
                    r, c = (dr + row), (dc + col)
                    if (r in range(rows) and 
                        c in range(cols) and 
                        (r,c) not in visit and
                        grid[r][c] == '1'):
                            q.append((r, c))
                            visit.add((r, c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    islands = islands + 1
                    bfs(r, c)

        # We are going over all the elements in the grid exactly once.
        # Hence the overall complexity is O(rows * cols)

        return islands


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(1, self.solution.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))


    def test_example_2(self):
        self.assertEqual(3, self.solution.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))



if __name__ == '__main__':
    unittest.main()

