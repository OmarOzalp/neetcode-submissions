# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        node = dummy
        carry = 0 
        while l1 or l2 or carry:
            l1_val = 0
            l2_val = 0
            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next
            node.next = ListNode((l1_val + l2_val + carry) % 10 )
            node = node.next
            if (l1_val + l2_val + carry) // 10 == 0:
                carry = 0
            else:
                carry = 1
            
            
            

        
        return dummy.next