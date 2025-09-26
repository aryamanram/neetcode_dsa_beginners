class ListNode():

    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.curr = ListNode(homepage)

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.curr.next = ListNode(url, self.curr)
        self.curr = self.curr.next

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val