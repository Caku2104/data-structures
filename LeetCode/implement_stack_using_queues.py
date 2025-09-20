# LeetCode 'Implement Stack using Queues' Exercise

from collections import deque

class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
    
    def push(self, x):
        self.queue1.append(x)

    def pop(self):
        if not self.empty():
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.popleft())

            result = self.queue1.popleft()
            self.queue1, self.queue2 = self.queue2, deque()
            
            return result
        
        raise IndexError("Pop from empty stack.")

    def top(self):
        if not self.empty():
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.popleft())
            
            result = self.queue1[0]
            
            self.queue2.append(self.queue1.popleft())
            self.queue1, self.queue2 = self.queue2, deque()
            
            return result
        
        raise IndexError("Top from empty stack.")

    def empty(self):
        return not self.queue1