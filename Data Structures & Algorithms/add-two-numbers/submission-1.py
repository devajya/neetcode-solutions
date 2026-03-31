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
        while l1 and l2:
            v1 = l1.val
            v2 = l2.val
            plus = v1+v2+carry
            digit = plus%10
            carry = plus//10
            curr.next = ListNode(digit)
            print("l3", digit)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            v1 = l1.val
            plus = v1+carry
            digit = plus%10
            carry = plus//10
            curr.next = ListNode(digit)
            print("l1", digit)
            curr = curr.next
            l1 = l1.next

        while l2:
            v2 = l2.val
            plus = v2+carry
            digit = plus%10
            carry = plus//10 
            curr.next = ListNode(digit)
            print("l3", digit)
            curr = curr.next
            l2 = l2.next

        if carry!= 0:
            curr.next = ListNode(carry)
            print("carry")
        
        return head.next
        