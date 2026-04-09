# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head.next == None or head == None:
            return
            
        # find middle
        slow = head
        fast = head 
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        

        # reverse second half
        before = None
        reverse = slow.next
        after = slow.next.next
        slow.next = None
        while after:
            reverse.next = before 
            before = reverse
            reverse = after
            after = reverse.next
        reverse.next = before
        last = reverse

        # merge
        curr = head
        while curr and last:
            temp = curr.next
            temp2 = last.next
            curr.next = last
            last.next = temp
            last = temp2
            curr = temp
    



        