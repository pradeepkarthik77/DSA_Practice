# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def symmetricUtil(p1,p2):

            if p1 is None and p2 is None:
                return True
            
            elif p1 is None or p2 is None:
                return False
            
            elif p1.val != p2.val:
                return False
            
            else:
                return symmetricUtil(p1.left,p2.right) and symmetricUtil(p1.right,p2.left)
        
        return symmetricUtil(root,root)