# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        answer = []

        def PathFinder(root,target,arr):
            
            if root is None:
                return
            
            if root.left is None and root.right is None:
                if target == root.val:
                    copyarr=arr.copy()
                    copyarr.append(root.val)
                    answer.append(copyarr.copy())
                return
            copyarr = arr.copy()
            copyarr.append(root.val)
            PathFinder(root.left,target-root.val,copyarr)
            PathFinder(root.right,target-root.val,copyarr)
            return
        
        PathFinder(root,targetSum,[])

        return answer