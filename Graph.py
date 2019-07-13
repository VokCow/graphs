import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class Graph(object):

    def __init__(self, adjList=None):
        if adjList == None:
            adjList = {}
        self.__adjList = adjList
        self.__tempvertices=[]
        self.__autoedges=[]

    def getVertices(self):
        return list(self.__adjList.keys())
    
    def getEdges(self): return self.__edgesList()
    
    def getAdjList(self): return self.__adjList

    def addVertex(self, vertex):
        if vertex not in self.__adjList:
            self.__adjList[vertex] = []
            self.__tempvertices.append(vertex)

    def addEdge(self, edge):
        vertex1,vertex2=edge[0],edge[1]
        if vertex1 in self.__adjList:
            self.__adjList[vertex1].append(vertex2)
        else:
            self.__adjList[vertex1] = [vertex2]
    
    def __edgesList(self):
        return [(vertex,vertices[i]) for vertex,vertices in self.__adjList.items() for i in range(len(vertices))]
    
    def draw(self):
        G=nx.Graph()
        G.add_node(0)
        edges=self.__edgesList()
        [G.add_edge(*edge) for edge in edges]
        [G.add_node(edge) for edge in self.__tempvertices]
        nx.draw(G,with_labels=True)
        plt.draw()
        plt.show()

    def getAdjencyMatrix(self):
        v=len(self.__adjList)
        A=np.zeros((v,v),int)
        for i in range(v):
            for j,v_row in self.__adjList.items():
                if v_row==[]: continue
                A[i,j]=int(i in v_row)
        return A
    
    def getLaplacianMatrix(self):
        v=len(self.__adjList)
        L=np.zeros((v,v),int)
        for v,vs in self.__adjList.items():
            if vs==[]: continue
            for w in vs:
                L[v,w],L[v,v]=-1,len(vs)
        return L
