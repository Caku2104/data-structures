"""

Implementation of a Doubly Linked List (DLL) in Python.

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            node.prev = current
        

    def prepend(self, data):
        node = Node(data)
    
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node


    def delete(self, key):
        current = self.head

        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    def display(self):
        current = self.head

        while current:
            print(f"{current.data} --> ", end= "")
            current = current.next
        
        print("None")


dll = DoublyLinkedList()

dll.prepend(5)
dll.display()

dll.append(10)
dll.append(25)
dll.display()

dll.prepend(50)
dll.display()

dll.delete(5)
dll.delete(25)
dll.display()