# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.totalsum = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def sumFinder(root,string):
            if root is None:
                return
            
            if root.left is None and root.right is None:
                string+=str(root.val)
                self.totalsum+=int(string)
                return
            
            string+=str(root.val)
            sumFinder(root.left,string)
            sumFinder(root.right,string)

        sumFinder(root,"")
        return self.totalsum