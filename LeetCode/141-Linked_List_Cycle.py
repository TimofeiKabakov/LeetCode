# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rabbit = head
        turtle = head
        
        while rabbit and rabbit.next:
            turtle = turtle.next
            rabbit = rabbit.next.next
            if rabbit == turtle:
                return True

        return False
