""" 
Simple Linked List implementation with insert, delete, search, and traversal methods.
"""

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def traverse(self):
        current = self.head
        while current:
            print(f"{current.data} --> ", end= "")
            current = current.next
        print("None")

    def insert_end(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return
    
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_beginning(self, value):
        new_node = Node(value)

        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        previous = None
        current = self.head

        while current:
            if current.data == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                print(f"Number {value} deleted.")
                return
            previous = current
            current = current.next
    

    def search(self, value):
        current = self.head
        
        while current:
            if current.data == value:
                return True
            else:
                current = current.next
        return False


ll = LinkedList()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_end(40)
ll.insert_end(50)
ll.traverse()

ll.insert_beginning(5)
ll.insert_beginning(0)
ll.traverse()

ll.delete(10)
ll.delete(30)
ll.traverse()

print(f"Number 40 is in the list. -> {ll.search(40)}")
print(f"Number 10 is in the list. -> {ll.search(10)}")