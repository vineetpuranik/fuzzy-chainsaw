Design a directed Graph class.

Your Graph class should support the following operations:

Graph() will initialize an empty directed graph.
void addEdge(int src, int dst) will add an edge from src to dst if it does not already exist. If either src or dst do not exist, add them to the graph.
bool removeEdge(int src, int dst) will remove the edge from src to dst if it exists. Return whether the edge was removed. Either src or dst may not exist in the graph.
bool hasPath(int src, int dst) will return whether there is a path from src to dst. Assume both src and dst exist in the graph.
Constraints:

Each vertex value will be a unique integer.
Multiple edges from one vertex to another are not allowed.
A vertex will not have an edge to itself, but the graph may contain a cycle.
The graph is not necessarily connected (there may be disconnected components).
Example 1:

Input:
["addEdge", 1, 2, "addEdge", 2, 3, "hasPath", 1, 3, "hasPath", 3, 1, "removeEdge", 1, 2, "hasPath", 1, 3]

Output:
[null, null, true, false, true, false]
Example 2:

Input:
["addEdge", 1, 2, "addEdge", 2, 3, "addEdge", 3, 1, "hasPath", 1, 3, "hasPath", 3, 1]

Output:
[null, null, null, true, true]