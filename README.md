
## Welcome to Graphs!

This is a Python project that contains a Graph class that allows several functionallity on undirected, non weighted graphs, such as adding edges, vertices and retrieve the Adjency and Laplacian Graph matrices.

## EXAMPLE USAGE:

**create graph from adjacency list:**
IN: G=Graph.Graph({0:[1],1:[0,2,3],2:[1],3:[1]})
create graph from edge list:

**G2 = Graph.Graph()**
[G2.addEdge(edge) for edge in [(0,1),(1,0),(1,3),(1,2),(3,1),(2,1)]]

## Methods:

* getVertices()
* getEdges()
* getAdjList()
* addVertex()
* addEdge()
* draw() [DEPRECATED-DEPENDENCE IN NETWORX PACKAGE]
* getAdjencyMatrix()
* getLaplacianMatrix()
