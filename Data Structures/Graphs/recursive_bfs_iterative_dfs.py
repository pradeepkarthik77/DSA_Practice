class Graph:

    def __init__(self,V):
        self.adj = {}
        self.V = V 
    
    def addEdge(self,u,v):
        
        if self.adj.get(u,False) == False:
            self.adj[u] = []
        
        self.adj[u].append(v)
    
    def bfs(self,element):

        def bfsUtil(visited,queue,arr):
            
            if not queue:
                return
            
            ele = queue.pop(0)

            arr.append(ele)

            for v in self.adj.get(ele,[]):
                if not visited.get(v,False):
                    queue.append(v)
                    visited[v] = True
            
            bfsUtil(visited,queue,arr)

        arr = []

        if self.V == 0:
            return []
    
        queue = [element]
        visited = {}

        visited[element] = True 

        bfsUtil(visited,queue,arr)

        return arr
    
    def dfs(self,element):

        if self.V == 0:
            return []

        stack = [element]

        arr = []

        visited = {}

        while stack:

            ele = stack.pop(0)

            visited[ele] = True

            arr.append(ele)

            for v in self.adj.get(ele,[]):
                if not visited.get(v,False):
                    stack.insert(0,v)
        
        return arr


if __name__=="__main__":
    g = Graph(5)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,3)
    g.addEdge(2,4)
    g.addEdge(3,4)
    g.addEdge(3,5)
    print(g.bfs(0))
    print(g.dfs(0))

