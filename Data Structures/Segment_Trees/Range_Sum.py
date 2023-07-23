import math
class SegmentTree:
    
    def __init__(self,N) -> None:
        m = 2**int(math.ceil(math.log2(N)))
        self.N = 2*m-1
        self.tree = [0]*self.N

    def construct(self,arr,beg,end,i):

        if beg > end:
            return 0

        elif beg == end:
            self.tree[i] = arr[beg]

        else:
            mid = (beg+end)//2
            left = 2*i+1
            right = 2*i+2

            leftsum = self.construct(arr,beg,mid,left)
            rightsum = self.construct(arr,mid+1,end,right)

            self.tree[i] = leftsum+rightsum
        
        return self.tree[i]

    def range_sum(self,u,v,beg,end,i):

        if end < u:
            return 0
        elif beg > v:
            return 0
        elif u <= beg and end <= v:
            return self.tree[i]
        elif beg == end:
            return self.tree[i]
        else:
            mid = (beg+end)//2
            left = 2*i+1
            right = 2*i+2

            return self.range_sum(u,v,beg,mid,left)+self.range_sum(u,v,mid+1,end,right)


if __name__ == "__main__":
    # arr = list(map(int,input("Enter the arr: ").split()))
    arr = [1,3,5,7,9,11]
    s = SegmentTree(len(arr))
    s.construct(arr,0,len(arr)-1,0)
    print(s.range_sum(0,3,0,len(arr)-1,0))