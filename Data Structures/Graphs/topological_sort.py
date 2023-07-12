class Graph:

    def __init__(self,V):
        self.adj = {}
        self.V = V 
    
    def addEdge(self,u,v):
        
        if self.adj.get(u,False) == False:
            self.adj[u] = []
        
        self.adj[u].append(v)
    
    def toposort(self):
        arr = []

        def topoUtil(visited,v):
            visited[v] = True 

            for i in self.adj.get(v,[]):
                if not visited.get(i,False):
                    topoUtil(visited,i)
            
            arr.append(v)

        visited = {}

        for i in range(self.V):
            if not visited.get(i,False):
                topoUtil(visited,i)
        
        return arr[::-1]


if __name__=="__main__":
    g = Graph(5)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,3)
    g.addEdge(2,4)
    g.addEdge(3,4)
    print("Is cycle present in graph: ",g.toposort())

