# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []

        ans = None
        ptr = ans
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        

        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        while stack1 or stack2 or carry:
            v1 = stack1.pop() if stack1 else 0
            v2 = stack2.pop() if stack2 else 0
            sum_to = v1 + v2 + carry
            digit = sum_to % 10
            carry = sum_to // 10

            new_node = ListNode(digit)
            new_node.next = ans
            ans = new_node
        
        return ans

        