"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        map = {}
        one = Node(head.val)
        two = one
        three = two
        curr = head

        map[curr] = one
        curr = curr.next

        while curr:
            one.next = Node(curr.val)
            one = one.next
            map[curr] = one
            curr = curr.next
        
        curr = head
        while two:
            temp = curr.random
            if not temp:
                two.random = None
            else:
                two.random = map[temp]
            
            curr = curr.next
            two = two.next
        return three
        
        
        
        
        