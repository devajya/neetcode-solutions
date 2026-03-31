"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        curr = head
        org_to_new = {}
        
        while curr:
            n = Node(curr.val)
            org_to_new[curr] = n
            curr = curr.next
        
        curr = head
        while curr:
            n = org_to_new[curr]
            n_1 = org_to_new[curr.next] if curr.next != None else None
            n_r = org_to_new[curr.random] if curr.random != None else None
            n.next = n_1
            n.random = n_r
            curr = curr.next

        return org_to_new[head]
        