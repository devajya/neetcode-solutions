# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hq


class Solution:    
    class Node(object):
        def __init__(self, n: ListNode):
            self.val = n.val
            self.next = n.next

        def __repr__(self):
            return f'Node value: {self.val}'

        def __lt__(self, other):
            return self.val < other.val

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        ans = ListNode()
        cur = ans
        for l in lists:
            hq.heappush(pq, self.Node(l))

        while len(pq) > 0:
            nde = hq.heappop(pq)
            val = nde.val
            print(val)
            ans.next = ListNode(val)
            ans = ans.next

            l_nde = nde.next
            if l_nde is not None:
                hq.heappush(pq, self.Node(l_nde))

        return cur.next
        