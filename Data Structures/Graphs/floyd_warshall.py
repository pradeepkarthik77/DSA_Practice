def floyd(adj,V):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                adj[i][j] = min(adj[i][j],adj[i][k]+adj[k][j])


if __name__=="__main__":

    edges = [[0,3,7],[3,0,2],[0,1,3],[1,0,8],[1,2,2],[2,0,5],[2,3,1]]

    V = 4

    adj = [[float('inf')]*V for i in range(V)]

    for u,v,w in edges:
        adj[u][v] = w
    
    for i in range(V):
        adj[i][i] = 0
    
    floyd(adj,V)

    print(adj)