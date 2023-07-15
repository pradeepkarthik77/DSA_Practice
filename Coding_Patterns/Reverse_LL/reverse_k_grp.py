# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        nde = head

        totalcount = 0

        while nde:
            nde = nde.next
            totalcount+=1
        
        totalcount = (totalcount)//k

        currhead = None
        prev = None

        count = 0

        allhead = None

        firstreversal = False

        headarr = []
        followarr = []
        currcount = 0
        while head:

            if allhead is None:
                allhead = head

            if currhead is None:
                currhead = head
                prev = head
                head = head.next
                currhead.next = None
            else:
                curr = head
                head = head.next
                curr.next = prev
                prev = curr
            
            count+=1

            if count == k:
                if not firstreversal:
                    allhead = prev
                    headarr.append(currhead)
                else:
                    headarr.append(currhead)
                    followarr.append(prev)
                firstreversal = True
                currcount +=1
                currhead = None
                count = 0
    
            if currcount == totalcount:
                followarr.append(head)
                break

        for i in range(len(headarr)):
            headarr[i].next = followarr[i]

        return allhead