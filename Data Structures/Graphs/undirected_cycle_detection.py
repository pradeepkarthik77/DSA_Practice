class Graph:

    def __init__(self,V):
        self.adj = {}
        self.V = V
    
    def addEdge(self,u,v):

        if self.adj.get(u,False) == False:
            self.adj[u] = []

        if self.adj.get(v,False) == False:
            self.adj[v] = []
        
        self.adj[u].append(v)
        self.adj[v].append(u)

    def isCyclic(self):

        def cycleUtil(v,visited,parent):
            
            visited[v] = True 

            for i in self.adj.get(v,[]):

                if not visited.get(i,False):
                    if cycleUtil(i,visited,v):
                        return True
                
                elif parent!=i:
                    return True
            
            return False

        visited = {}
        parent = -1

        return cycleUtil(0,visited,parent)

if __name__=="__main__":

    g = Graph(5)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,3)
    g.addEdge(2,4)
    g.addEdge(3,4)
    print("Is there a cycle in undirtected graph: ",g.isCyclic())
