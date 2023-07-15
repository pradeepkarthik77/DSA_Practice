def triplet_sum(nums,target):
    nums.sort()

    n = len(nums)

    closestsum = float('inf')

    for i in range(n):
        
        l,r = i+1,n-1

        while l<r:
            sum = nums[i]+nums[l]+nums[r]

            currclose = abs(target-sum)

            if currclose < closestsum:
                closestsum = currclose
                
            if sum > target:
                r-=1
            else:
                l+=1
        
    return closestsum

if __name__=="__main__":
    arr = [-2,0,1,2]
    target = 2
    print(triplet_sum(arr,target))


            