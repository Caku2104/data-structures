# LeetCode Valid Parentheses Solution

class Solution(object):

    def __init__(self):
        self.characters = []

    def push(self, new_item):
        self.characters.append(new_item)

    def pop(self):
        if not self.is_empty():
            return self.characters.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.characters[-1]
        return None
    
    def is_empty(self):
        return len(self.characters) == 0

    def isValid(self, s):
        combinations = {')':'(', ']':'[', '}':'{'}

        for ch in s:
            if ch in combinations.values():
                self.push(ch)
            elif ch in combinations.keys():
                if self.peek() == combinations[ch]:
                    self.pop()
                else:
                    return False
        return self.is_empty()