class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root ):
        # Code here
        
        if root is None:
            return []
            
        queue = [root]
        arr = []
        while queue:
            v = queue.pop(0)
            arr.append(v.data)
            
            if v.left:
                queue.append(v.left)
            if v.right:
                queue.append(v.right)
            
        return arr