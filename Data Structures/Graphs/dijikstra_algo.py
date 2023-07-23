class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        
        def dfs(u,distance,visited,adj,execcount,V):
            
            execcount += 1
            visited[u] = True
            
            mindist = float('inf')
            min_v = -1
            
            for v,w in adj[u]:
                distance[v] = min(distance[v],distance[u]+w)
            
            for i in range(len(distance)):
                if distance[i] < mindist and visited[i] == False:
                    mindist = distance[i]
                    min_v = i
            
            if min_v == -1:
                return
            elif execcount == V:
                return
            else:
                dfs(min_v,distance,visited,adj,execcount,V)
        
        distance = [float('inf')]*V
        
        visited = [False]*V
        
        distance[S] = 0
        
        dfs(S,distance,visited,adj,0,V)
        
        return distance


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends