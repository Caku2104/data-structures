# LeetCode '232. Implement Queue using Stacks' Problem

class MyQueue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, item):
        self.in_stack.append(item)

    def pop(self):
        if self.empty():
            raise IndexError("Cannot pop from an empty queue.")
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self):
        if self.empty():
            raise IndexError("Cannot peek to an empty queue.")
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self):
        return len(self.out_stack) == 0 and len(self.in_stack) == 0