class Graph:

    def __init__(self,V):
        self.adj = {}
        self.V = V 
    
    def addEdge(self,u,v):
        
        if self.adj.get(u,False) == False:
            self.adj[u] = []
        
        self.adj[u].append(v)
    
    def findcycle(self):

        def cycleUtil(v,visited):
            
            visited[v] = True

            boole = False

            for i in self.adj.get(v,[]):
                if visited.get(i,False):
                    return True
                else:
                    boole = boole or cycleUtil(i,visited)

            return boole
            
        visited = {}

        return cycleUtil(0,visited)


if __name__=="__main__":
    g = Graph(5)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,3)
    g.addEdge(2,4)
    g.addEdge(3,4)
    print("Is cycle present in graph: ",g.findcycle())

