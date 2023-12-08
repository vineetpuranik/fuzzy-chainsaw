## Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 
## Examples
Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: falseit
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

## Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

## Algorithm
1. If len(preq) is 0 then immediately return true.
2. Create a graph from prerequisites 2D array. Use dictionary in python. 
3. While creating the graph if there is a self dependency i.e. a self edge then immediately return False
4. Add directed edges from preq[i][1] preq[i][0] indicating 1 is needed to be completed before 0
4. Run DFS and explore on the graph. 
5. Check for any back edges and return False if a backedge exists. For e(u, v) if post[u] < post[v] a backedge exists. 
6. When a graph has a backedge then definitely there is a cyle and for our problem if we encounter a cycle that means it is impossible to complete the courses. 