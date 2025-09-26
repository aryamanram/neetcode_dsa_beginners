class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and curr != self.right and index == 0:
            return curr.val
        return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        node, next, prev, = ListNode(val), self.left.next, self.left
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        node, next, prev, = ListNode(val), self.right, self.right.prev
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            node, next, prev, = ListNode(val), curr, curr.prev
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.right and index == 0:
            next, prev = curr.next, curr.prev
            next.prev = prev
            prev.next = next