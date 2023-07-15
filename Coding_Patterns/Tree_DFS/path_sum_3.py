# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.paths = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def PathFinder(root,targetSum,arr):

            if root is None:
                return
            
            copyarr = arr.copy()

            copyarr.append(root.val)

            sum = 0

            for i in range(len(copyarr)-1,-1,-1):
                sum+=copyarr[i]
                if sum == targetSum:
                    self.paths+=1
        
            PathFinder(root.left,targetSum,copyarr)
            PathFinder(root.right,targetSum,copyarr)
        
        PathFinder(root,targetSum,[])
        return self.paths