# create adjacency list
# explore all nodes

class Solution(object):
    def countComponents(self, n, edges):
        # created an adjacency list
        adjaceny_list = {}
        visited = set()
        output = 0
        
        for i in range(n):
            adjaceny_list[i] = []
        
        for edge in edges:
            adjaceny_list[edge[0]].append(edge[1])  
            adjaceny_list[edge[1]].append(edge[0])
        
        def explore(node, visited):
            visited.add(node)
            for edge in adjaceny_list[node]:
                if edge not in visited:
                    explore(edge, visited)
                    
        # print(adjaceny_list)
        for node in adjaceny_list.keys():
            if node not in visited:
                output += 1
                explore(node, visited)
                
        return output
        
