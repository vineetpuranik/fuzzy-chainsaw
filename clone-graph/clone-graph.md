## Clone graph
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}


## Constraints

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.


## Algorithm

1. Create a hash map that will map the node in the input graph to the new cloned node. 
2. Run DFS starting from the input node. 
3. For each iteration of DFS check if the node being iterated exists in the hashmap if yes, then return the node. 
4. If it does not exist, create a clone then add the node to the hashmap and call dfs on its neighbors. 