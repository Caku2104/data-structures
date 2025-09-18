
# 'Reverse Linked List' Exercise

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    
    def reverseList(self, head):
        prev = None
        current = head

        while current:
            next_el = current.next
            current.next = prev
            prev = current
            current = next_el

        return prev
