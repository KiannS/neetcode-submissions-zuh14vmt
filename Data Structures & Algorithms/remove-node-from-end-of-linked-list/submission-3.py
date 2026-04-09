# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None or head == None:
            return
        if n == 1:
            res = head
            curr = head
            while curr:
                if curr.next.next == None:
                    curr.next = None
                curr = curr.next
            return head
        
        before = None
        curr = head
        after = curr.next
        count = 1

        while after:
            curr.next = before
            before = curr
            curr = after
            after = curr.next
        curr.next = before
        head = curr

        while curr and curr.next:

            if count == n - 1:
                curr.next = curr.next.next

            count += 1
            curr = curr.next
        
        before = None
        curr = head
        after = curr.next
        while after:
            curr.next = before
            before = curr
            curr = after
            after = curr.next
        curr.next = before

        return curr
        
        
        




