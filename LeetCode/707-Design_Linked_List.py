class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None 

class MyLinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        i = 0
        node = self.left.next
        while node and node != self.right:
            if i == index:
                return node.val
            node = node.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        cur, prev_node, next_node = ListNode(val), self.left, self.left.next
        prev_node.next = cur
        next_node.prev = cur
        cur.next = next_node
        cur.prev = prev_node

    def addAtTail(self, val: int) -> None:
        cur, prev_node, next_node = ListNode(val), self.right.prev, self.right
        prev_node.next = cur
        next_node.prev = cur
        cur.next = next_node
        cur.prev = prev_node

    def addAtIndex(self, index: int, val: int) -> None:
        i = 0
        node = self.left.next
        while node:
            if i == index:
                cur, prev_node, next_node = ListNode(val), node.prev, node
                prev_node.next = cur
                next_node.prev = cur
                cur.next = next_node
                cur.prev = prev_node
            node = node.next
            i += 1

    def deleteAtIndex(self, index: int) -> None:
        i = 0
        node = self.left.next
        while node and node != self.right:
            if i == index:
                prev_node, next_node = node.prev, node.next
                prev_node.next = next_node
                next_node.prev = prev_node
            node = node.next
            i += 1
    
    def printList(self):
        i = 0
        node = self.left.next
        res = []
        while node and node != self.right:
            res.append(node.val)
            node = node.next
            i += 1
        print(res)