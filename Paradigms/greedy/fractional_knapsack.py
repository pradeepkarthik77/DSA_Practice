def find_profit(arr,W):

    arr.sort(key=lambda k:(k[0]/k[1]),reverse=True)

    profit = 0

    for p,w in arr:
        if w > W:
            profit+=(W)*(p/w)
            W = 0
            break
        else:
            profit+= p
            W-=w 
    
    return profit
        



if __name__ == "__main__":
    W = 50
    arr = [[60,10],[100,20],[120,30]]
    print(find_profit(arr,W))