# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode(-1)
        curr = head
        while True:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            plus = v1+v2+carry
            digit = plus%10
            carry = plus//10
            curr.next = ListNode(digit)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if not l1 and not l2:
                break

        if carry!= 0:
            curr.next = ListNode(carry)
        
        return head.next
        