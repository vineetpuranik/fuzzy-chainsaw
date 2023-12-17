class Graph:
    # each vertex value will be a unique integer
    # multiple edges from one vertex to another are not allowed
    # no self edges
    # graph is not necessarily connected. It may be disconnected as well
    
    def __init__(self):
        # we will be using adjacency list for storing our graph
        self.g = {}


    def addEdge(self, src: int, dst: int) -> None:
        # first we need to make sure that both src and dst are present in our graph as vertices
        if src not in self.g:
            self.g[src] = []

        if dst not in self.g:
            self.g[dst] = []

        # we will add edge from src to dst only if it does not exist in the graph
        srcEdgeList = self.g[src]
        dstExists = False

        for edge in srcEdgeList:
            # if edge is present then dstExists to True
            if edge == dst:
                dstExists = True
                break

        if dstExists == False:
            # edge does not exist then add it to the edge list
            self.g[src].append(dst)
        
        return
                     
    def removeEdge(self, src: int, dst: int) -> bool:
        # if src or dst vertices do not exist in the graph then return false
        if (src not in self.g) or (dst not in self.g):
            return False

        # if we reach here that means both src and dst are present as vertices in our graph
        # find if the edge from src to dst exists in our graph
        for index, edge in enumerate(self.g[src]):
            # if we find the edge to be removed then remove the edge
            if edge == dst:
                del self.g[src][index]
                return True

        return False        



    def hasPath(self, src: int, dst: int) -> bool:
        # return True if path exists from src to dst
        # we need to assume that both src and dst exist in the graph

        # general idea start explore from src. 
        # at the end of explore, if visited set contains dst then return True
        # else return False

        # set to store all the vertices visited when we start exploration from the src vertex
        visited = set()
        
        # explore all the vertices reachable from the start vertex
        def explore(start):
            # add the current vertex to visited set
            visited.add(start)

            # explore all the neighbor of the current vertex
            for neighbor in self.g[start]:
                if neighbor not in visited:
                    explore(neighbor)        
        

        # call explore from the src vertex
        explore(src)
        
        # visited contains dst vertex that means there exists a path from src to dst and hence return True
        if dst in visited:
            return True

        # visited does not contain dst. This implies that there is no path from src to dst    
        else:
            return False    







