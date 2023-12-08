from typing import List

# inner functions dont need to have self passed in
# simple variables like clock need to have nonlocal clock declared in the inner function in order to modift them 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if there are no prereqs return true
        if len(prerequisites) == 0:
            return True
        
        # declare a dictionary for the graph
        g = {}
        
        # populate nodes in our graph
        for i in range(0, numCourses):
            g[i] = []
            
        # add directed edges
        for i in range(len(prerequisites)):
            #check for self referential courses. If found immediately return false
            if prerequisites[i][1] == prerequisites[i][0]:
                return False
            
            # add directed edge from prerequisites[i][1] -> prerequisites[i][0] since we need to take 1 before we can take 0
             
            g[prerequisites[i][1]].append(prerequisites[i][0])
       
        
        # create 2 dictionaries for storing the post order and pre order numbers of the traversal
        pre = {}
        post = {}
        clock = 1
        visited = set()
        
        def dfs(g):
            for v in g:
                if v not in visited:
                    explore(v)
        
        
        def explore(v):
            nonlocal clock
            pre[v] = clock
            clock += 1
            visited.add(v)
            for e in g[v]:
                if e not in visited:
                    explore(e)
            post[v] = clock
            clock += 1
            
        dfs(g)
        
        #check pre order and post order numbers
        for v in g:
            for e in g[v]:
                if post[v] < post[e]:
                    # indicates a backedge and that means the graph has a cycle
                    return False
        return True
        
        
        
            
            