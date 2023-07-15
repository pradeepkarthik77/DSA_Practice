# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def PathFinder(root,target):
            if root is None:
                return False
            
            if root.left is None and root.right is None:
                return target == root.val
            
            leftboole = False
            rightboole = False

            if root.left:
                leftboole = PathFinder(root.left,target-root.val)
            
            if root.right:
                rightboole = PathFinder(root.right,target-root.val)
            
            return leftboole or rightboole
        
        return PathFinder(root,targetSum)