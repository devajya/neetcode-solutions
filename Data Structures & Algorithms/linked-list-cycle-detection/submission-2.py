# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_p = head
        if not head or not head.next:
            return False
        fast_p = head.next

        while slow_p and fast_p:
            if slow_p == fast_p:
                return True
            slow_p = None if slow_p == None else slow_p.next
            fast_p = None if fast_p.next == None else fast_p.next.next

        return False