# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self,head):
        prev = None
        temp = head

        newhead = None

        while temp:
            curr = temp
            temp = temp.next
            curr.next = prev
            prev = curr

        return curr


    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        oldslow = slow

        slow = self.reverseList(slow)

        fast = head

        curr = None

        while fast and slow and fast!=oldslow:
            print(fast.val,slow.val)
            if curr is None:
                curr = fast
            else:
                curr.next = fast
                curr = fast

            fast = fast.next

            curr.next = slow
            curr = curr.next
            slow = slow.next
            
        return head

