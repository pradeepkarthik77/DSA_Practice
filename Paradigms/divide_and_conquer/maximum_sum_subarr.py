class Solution:

    def findacross(self,nums,beg,mid,end):

        leftsum = float('-inf')
        rightsum = float('-inf')

        currsum = 0

        for i in range(mid,beg-1,-1):
            currsum+= nums[i]
            if currsum > leftsum:
                leftsum = currsum

        currsum = 0

        for i in range(mid,end+1):
            currsum+=nums[i]
            if currsum > rightsum:
                rightsum = currsum
        
        return max(leftsum,rightsum,leftsum+rightsum-nums[mid])
            

    def findmax(self,nums,beg,end):
        if beg > end:
            return float('-inf')
        if beg == end:
            return nums[beg]
        if beg<end:
            mid = (beg+end)//2

            leftsum = self.findmax(nums,beg,mid)
            rightsum = self.findmax(nums,mid+1,end)

            acrosssum = self.findacross(nums,beg,mid,end)

            return max(leftsum,rightsum,acrosssum)

    def maxSubArray(self, nums: List[int]) -> int:
        # print(self.findmax(nums,0,len(nu)))
        return self.findmax(nums,0,len(nums)-1)