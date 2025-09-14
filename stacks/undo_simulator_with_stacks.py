# Undo Feature Simulator

class Stack:

    def __init__(self):
        self.commands = []

    def push(self, command):
        self.commands.append(command)
        print(f"Pushed: {command}")
    
    def pop(self):
        if not self.is_empty():
            command = self.commands.pop()
            return command
        raise IndexError("Invalid operation: pop from empty stack")
    
    def is_empty(self):
        return len(self.commands) == 0
    
    def print_stack(self):
        print("Current Stack:", self.commands)

def main():
    stack = Stack()

    while True:
        input_command = input("Enter a command to push onto the stack (or 'undo' to remove the previous, 'exit' to quit): ").strip().lower()

        if input_command == "exit":
            print("Exiting program.")
            break
        elif input_command == "undo":
            try:
                print(f"Removing: {stack.pop()}")
                if stack.is_empty():
                    print("Stack is now empty.")
                else:
                    stack.print_stack()
            except IndexError as e:
                print(e)
        else:
            stack.push(input_command)
            stack.print_stack()

if __name__ == "__main__":
    main()
