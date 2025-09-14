
#       Expression Evaluator using Stack

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0



def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False

def evaluate_expression(expression, stack):
    tokens = expression.split()

    for token in tokens:
        if is_number(token):
            stack.push(float(token))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            if token == '+':
                result = num1 + num2
                stack.push(result)
            elif token == '-':
                result = num1 - num2
                stack.push(result)
            elif token == '*':
                result = num1 * num2
                stack.push(result)
            elif token == '/':
                if num2 == 0:
                    print("Error: Division by zero")
                    return None
                result = num1 / num2
                stack.push(result)
            else:
                print(f"Unknown operator: {token}")

    if not stack.is_empty():
        return stack.pop()
    return None

def main():
    stack = Stack()

    expression = "3 5 * 2 + 8 - 7 / "

    result = evaluate_expression(expression, stack)
    
    if result == None:
        print("The stack is empty.")
    else:
        print(f"The result of the expression '{expression}' is: {result:.1f}")

if __name__ == "__main__":
    main()