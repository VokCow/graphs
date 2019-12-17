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
		self.

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
    

#         D = np.zeros((v,v),int)
#         for v,vs in self.__adjList.items():
#             if vs==[]: continue
#             for w in vs:
#                 L[v,v]=len(vs)
        
    
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
        D=self.getDMatrix()
		A=self.getAdjencyMatrix()
        return D-A

    def getDMatrix(self):
	    v=len(self.__adjList)
		D=np.zeros(v)
		vs=[len(val) for val in self.__adjList.values()]
		D[np.diag_indices(v)]=vs
        return D
     
    

def AdjMfromGrayImage(I):
# Returns the (sparse) adjency matrix of the Graph formed connecting all pixels in an image with their horizontal, vertical and diagonal neighbours
# , weighted by Gaussian weights.
  Tetha=.1
  def dist(pixeldiff):  
    return np.exp(-np.square(pixeldiff)/(2*Tetha**2))

  # calculates differences between all adjacent elements in an nxn array 
  N=I.shape[0]
  hdif=I[:,1:]-I[:,:N-1] # horizontal differences
  vdif=I[1:,:]-I[:N-1,:] # vertical differences
  dpdif=I[1:,1:]-I[:N-1,:N-1] # differences parallel to main diagonal
  dsdif=I[:N-1,1:]-I[1:,:N-1] # differences parallel to secondary diagonal
  hdif,vdif,dpdif,dsdif=dist(np.ravel(hdif)),dist(np.ravel(vdif)),dist(np.ravel(dpdif)),dist(np.ravel(dsdif))

  row,col=np.diag_indices(N)

  AdjM=np.zeros((N**2,N**2)) # intialize adjency matrix

  mblock_idxs=[n*N for n in range(N)] # create indexes for main blocks

  start,step,end=0,N-1,N-1

  # Blocks forming "main Block diagonal" These blocks are NxN matrices with all zero entries except those up the main diagonal, that are
  # equal to the differences between horizontally adjacent pixels in the image.

  for idx in mblock_idxs:

    mblock=np.zeros((N,N)) # initialize mblock
    mblock[row[:N-1],col[1:]]=hdif[start:end] # fill main block with differences

    start+=step
    end+=N-1

    AdjM[idx:idx+N,idx:idx+N]=mblock # fill main blocks

  dblock_idxs=[n*N for n in range(N-1)] # create indexes for diag blocks


  # Blocks Up and Down of "Main Block Diagonal". These blocks are NxN zero matrices with all zero entries except those at the main diagonal, that are equal
  # to the differences between vertically adjacent pixels in the image, the entries up the main diagonal, equal to the differences between right-diagonally
  #  adjacent pixels, and the entries down the main diagonal, equal to differences between left-diagonally adjacent pixels.

  ix = 0
  start,step,end=0,N-1,N-1

  for idx in dblock_idxs:
    # diagonal block

    sblock=np.zeros((N,N))

    sblock[row,col]=vdif[ix*N:(ix+1)*N]
    sblock[row[1:],col[:N-1]]=dsdif[start:end] 
    sblock[row[:N-1],col[1:]]=dpdif[start:end]

    ix+=1
    start+=step
    end+=N-1

    AdjM[idx:idx+N,idx+N:idx+2*N]=sblock
    AdjM[idx+N:idx+2*N,idx:idx+N]=sblock

  return AdjM
