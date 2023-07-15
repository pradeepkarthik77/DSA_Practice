# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if root is None:
            return []
        
        queue = [root]
        nextqueue = []
        
        averages = []

        curravg = 0
        currcount = 0

        while queue:
            v = queue.pop(0)
            curravg += v.val
            currcount +=1
            if v.left:
                nextqueue.append(v.left)
            if v.right:
                nextqueue.append(v.right)
            
            if not queue:
                queue = nextqueue.copy()
                nextqueue = []

                averages.append(curravg/currcount)
                curravg = 0
                currcount = 0
        
        return averages
