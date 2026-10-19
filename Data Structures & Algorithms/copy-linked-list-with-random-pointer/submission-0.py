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

        # what we can do is this

        dummy = Node(0)
        tail = dummy 
        cur = head

        old_to_new = {None:None}

        while cur:
            tail.next = Node(cur.val)
            old_to_new[cur] = tail.next
            tail = tail.next
            cur = cur.next
        
        start = head
        start1 = dummy.next
        while start:
            start1.random = old_to_new[start.random]
            start1 = start1.next
            start = start.next
        
        return dummy.next

        

        