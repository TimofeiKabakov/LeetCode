# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyNode = ListNode(-1, head)
        
        current = dummyNode

        while(current.next):
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
         
        return dummyNode.next