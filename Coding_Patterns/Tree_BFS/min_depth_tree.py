# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def depthUtil(root,depth):
            if root is None:
                return float('inf')
            
            if root.left is None and root.right is None:
                return depth
            
            depth1 = depthUtil(root.left,depth+1)
            depth2 = depthUtil(root.right,depth+1)

            if depth1>0 and depth1<=depth2:
                return depth1
            elif depth2>0 and depth2<depth1:
                return depth2
            else:
                return 0
        
        depth = 1
        depth = depthUtil(root,depth)
        if depth == float('inf'):
            depth = 0
        
        return depth