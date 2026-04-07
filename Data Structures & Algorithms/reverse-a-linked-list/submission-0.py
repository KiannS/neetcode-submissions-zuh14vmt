# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return None
        if head.next == None:
            return head
        
        before = None
        after = head.next
        curr = head

        while after != None:
            curr.next = before
            before = curr
            curr = after
            after = after.next
        curr.next = before

        return curr
        




        
        

        