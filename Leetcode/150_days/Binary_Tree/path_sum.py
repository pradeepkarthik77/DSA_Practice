# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def SumFinder(root,targetSum,sum):

            if root is None:
                return False
            
            elif root.left is None and root.right is None:
                return (targetSum) == (sum+root.val)
            
            else:
                boole1 = SumFinder(root.right,targetSum,sum+root.val)
                boole2 = SumFinder(root.left,targetSum,sum+root.val)
                return boole1 or boole2
        
        if root is None:
            return False

        return SumFinder(root,targetSum,0)