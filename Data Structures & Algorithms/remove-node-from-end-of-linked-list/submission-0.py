# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # What we can do is move the first down n nodes. 
        # then once it reaches there. then we can move both. the
        # dummy, 1, 2, 3, 4 -> second node from the end. 
        start = ListNode()
        start.next = head
        s = start
        f = head
        i = 0 
        #n = 3
        while f:
            if i < n: 
                f = f.next
                i+=1
            else:
                s = s.next
                f = f.next
        
        s.next = s.next.next

        return start.next
            

        
        
        