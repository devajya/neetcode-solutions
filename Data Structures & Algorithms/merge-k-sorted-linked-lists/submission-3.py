# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    class CompareNode:
        def __init__(self, n:ListNode):
            self.val = n.val
            self.next = n.next
        
        def __lt__(self, other):
            return self.val < other.val

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        ans = ListNode()
        ptr = ans
        for l in lists:
            heapq.heappush(heap, self.CompareNode(l))
        
        while len(heap) > 0:
            cnode = heapq.heappop(heap)
            val = cnode.val

            ptr.next = ListNode(val)
            ptr = ptr.next

            if cnode.next:
                heapq.heappush(heap, self.CompareNode(cnode.next))
        return ans.next
