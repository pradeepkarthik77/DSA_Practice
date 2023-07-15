# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        currqueue = [root]

        nextqueue = []

        answer = []

        temp = []

        while currqueue:

            v = currqueue.pop(0)

            temp.append(v.val)

            if v.left is not None:
                nextqueue.append(v.left)
            if v.right is not None:
                nextqueue.append(v.right)
            
            if not currqueue:
                currqueue = nextqueue.copy()
                nextqueue = []
                answer.append(temp.copy())
                temp = []
        
        return answer