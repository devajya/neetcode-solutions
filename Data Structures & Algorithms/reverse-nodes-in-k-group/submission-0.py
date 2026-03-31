# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_p = dummy #0
        while True:
            group_end = self.findK(prev_p, k)
            if not group_end:
                break
            end_next_p = group_end.next #1

            prev = group_end.next
            curr = prev_p.next

            while curr != end_next_p:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            outer_temp = prev_p.next
            prev_p.next = group_end
            prev_p = outer_temp

        return dummy.next

    def findK(self, nde: Optional[ListNode], k: int) -> Optional[ListNode]:
        while nde and k>0:
            nde = nde.next if nde else None
            k-=1
        return nde