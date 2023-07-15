# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = [float('-inf')]

        def MaxPath(root):

            if root is None:
                return 0
            
            leftsum = max(MaxPath(root.left),0)
            rightsum = max(MaxPath(root.right),0)

            res[0] = max(res[0],leftsum+rightsum+root.val)

            if res[0] == root.val+leftsum:
                print(root.val,rightsum,leftsum)

            return root.val+max(leftsum,rightsum)

        MaxPath(root)
        return res[0]