# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find Mid
        def find_mid(head):
            s = head
            f = head
            while f and f.next:
                s = s.next
                f = f.next.next
            
            second = s.next
            s.next = None
            return second
        # 2. Reverse list
        def reverse_list(l):
            prev = None
            curr = l

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            return prev

        l2 = reverse_list(find_mid(head))
        l1 = head
        while l2:
            n1, n2 = l1.next, l2.next
            l1.next = l2
            l2.next = n1
            l1, l2 = n1, n2






        