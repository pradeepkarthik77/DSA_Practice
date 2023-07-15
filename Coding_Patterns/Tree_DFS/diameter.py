# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def diameter(root):
            if root is None:
                return 0

            leftdiameter = diameter(root.left)
            rightdiameter = diameter(root.right)

            self.answer = max(self.answer,leftdiameter+rightdiameter)
            return max(leftdiameter,rightdiameter)+1
    
        diameter(root)

        return self.answer
            