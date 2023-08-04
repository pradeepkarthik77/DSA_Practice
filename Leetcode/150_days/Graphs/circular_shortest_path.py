'''
Find the minimum cost of traveling between 2 tram stationns in a circular city with N stations numbered  1 to N .

the cost of tickets between adjacent stations is given as array ticket _cost  where ticket cost,
[I] represent the cost of traveling from I to I+1%N station .
trams can move in both directions.

imput includes start,finish,N,ticket_cost . Output should return the minimum cost of traveling from start to finish

'''
def findedges(N,arr):
    
    edges = []
    
    for i in range(N):
        edges.append([i,((i+1)%N),arr[i]])
    
    return edges

def findcost(N,src,dest,arr):
    
    edges = findedges(N,arr)
    
    dist = [float('inf') for i in range(N)]
    
    dist[src-1] = 0
    
    for u,v,w in edges:
        dist[v] = min(dist[v],dist[u]+w)
    
    return dist[dest-1]

if __name__=="__main__":
    
    arr = [1,2,3,4]
    N = 4
    src = 1 
    dest = 3
    print(findcost(N,src,dest,arr))
    
