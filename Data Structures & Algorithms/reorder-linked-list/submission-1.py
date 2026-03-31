# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle of the list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next if slow else None
            fast = fast.next.next if fast.next else None

        curr=slow.next
        prev = None
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        while prev:
            t1 = head.next
            t2 = prev.next
            head.next = prev
            prev.next = t1
            head = t1
            prev = t2
        




        
        
