# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        i = 0
        while curr:
            i+=1
            curr = curr.next
        
        idx_ahead_of_r = i-n-1
        print(idx_ahead_of_r)

        if idx_ahead_of_r < 0:
            return head.next
        
        curr = head
        while idx_ahead_of_r:
            curr = curr.next
            idx_ahead_of_r-=1
        curr.next = curr.next.next

        return head
