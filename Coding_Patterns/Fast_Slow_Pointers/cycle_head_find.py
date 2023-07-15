# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        hare = head
        tort = head

        boole = False

        while hare and tort and hare.next:

            hare = hare.next.next
            tort = tort.next

            if hare == tort:
                boole = True
                break


        if boole:
            tort = head

            while hare and tort:

                if hare == tort:
                    return hare
                
                hare = hare.next
                tort = tort.next
        
        return None
