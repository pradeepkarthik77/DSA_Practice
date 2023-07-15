"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if root is None:
            return None
        
        head = root

        prev = None

        queue = [root]
        nextqueue = []

        while queue:
            v = queue.pop(0)

            if prev is None:
                prev = v
            else:
                prev.next = v
                prev = v
            
            if v.left:
                nextqueue.append(v.left)
            if v.right:
                nextqueue.append(v.right)
            
            if not queue:
                queue = nextqueue.copy()
                nextqueue = []
                prev.next = None
                prev = None
                
        return head