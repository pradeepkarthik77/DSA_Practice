# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def maxUtil(node):
            if node is None:
                return 0
            
            else:
                rightdepth = maxUtil(node.right)
                leftdepth = maxUtil(node.left)

                return max(rightdepth,leftdepth)+1

        return maxUtil(root)