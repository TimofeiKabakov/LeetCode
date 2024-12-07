class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        next_iter = None
        while(head):
            next_iter = head.next
            head.next = prev
            prev = head
            head = next_iter
        return prev

# Time Complexity: O(n)
# Space Complexity: O(1)