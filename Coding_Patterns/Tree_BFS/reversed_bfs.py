# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = [root]

        if root is None:
            return []
        
        nextqueue = []

        temp = []
        answer = []

        while queue:
            v = queue.pop(0)

            temp.append(v.val)

            if v.left:
                nextqueue.append(v.left)
            if v.right:
                nextqueue.append(v.right)
            
            if not queue:
                queue = nextqueue.copy()
                nextqueue = []
                answer.append(temp.copy())
                temp = []
        
        return answer[::-1]