# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        head = curr
        
        while list1 and list2:
            print("reached")
            if list1.val < list2.val:
                ptr = list1
                list1 = list1.next
                ptr.next = None
            else:
                ptr = list2
                list2 = list2.next
                ptr.next = None

            curr.next = ptr
            curr = curr.next
            print(curr.val)

        while list1:
            ptr = list1
            list1 = list1.next
            ptr.next = None
            curr.next = ptr
            curr = curr.next

        while list2:
            ptr = list2
            list2 = list2.next
            ptr.next = None
            curr.next = ptr
            curr = curr.next

        return head.next