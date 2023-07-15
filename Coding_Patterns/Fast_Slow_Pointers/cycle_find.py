# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        hare = head
        tort = head

        while hare and tort and hare.next:

            hare = hare.next.next
            tort = tort.next

            if hare == tort:
                return True
            
        return False
