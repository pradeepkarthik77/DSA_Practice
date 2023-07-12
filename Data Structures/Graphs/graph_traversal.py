class Graph:

    def __init__(self,V):
        self.adj = {}
        self.V = V 
    
    def addEdge(self,u,v):
        
        if self.adj.get(u,False) == False:
            self.adj[u] = []
        
        self.adj[u].append(v)
    
    def bfs(self,element):

        arr = []
        
        if self.V <1:
            return []

        queue = [element]

        visited = {}

        while len(queue)!=0:

            ele = queue.pop(0)

            arr.append(ele)

            for v in self.adj.get(ele,[]):
                if visited.get(v,False) == False:
                    visited[v] = True
                    queue.append(v)

        return arr
    
    def dfs(self,element):

        def dfsUtil(visited,arr,v):

            visited[v] = True 

            arr.append(v)

            for nde in self.adj.get(v,[]):
                if not visited.get(nde,False):
                    dfsUtil(visited,arr,nde)
        
        arr = []

        visited = {}

        dfsUtil(visited,arr,element)

        return arr


if __name__=="__main__":
    g = Graph(5)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,3)
    g.addEdge(2,4)
    g.addEdge(3,4)
    print(g.bfs(0))
    print(g.dfs(0))

