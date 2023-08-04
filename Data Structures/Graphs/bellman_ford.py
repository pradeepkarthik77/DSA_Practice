class Graph:
    def __init__(self,V):
        self.V = V 
        self.adj = [[] for i in range(self.V)]

    def addEdge(self,u,v,w):
        self.adj[u].append([v,w])
    
    def returnEdges(self):
        edges = []
        for indx,inEdge in enumerate(self.adj):
            for edge in inEdge:
                edges.append([indx,edge[0],edge[1]])
        return edges
    
    def BellmanFord(self,src):

        edges = self.returnEdges()
        
        dist = [float('inf') for i in range(self.V)]
        dist[src] = 0

        for u,v,w in edges:
            dist[v] = min(dist[v],dist[u]+w)
        
        return dist


if __name__=="__main__":
    g = Graph(5)
    g.addEdge(0, 1, -1)
    g.addEdge(0, 2, 4)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 3, 2)
    g.addEdge(1, 4, 2)
    g.addEdge(3, 2, 5)
    g.addEdge(3, 1, 1)
    g.addEdge(4, 3, -3)

    print(g.BellmanFord(0))