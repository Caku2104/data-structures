# LeetCode '155. Min Stack' Problem

class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        """

        Pushing values as tuples in the form (minimum in stack, value)
        
        """
        if not self.stack:
            current_min = val
        else:
            current_min = min(val, self.stack[-1][0])
        
        self.stack.append((current_min, val))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][1]
    
    def getMin(self):
        return self.stack[-1][0]