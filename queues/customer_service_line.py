# Customer Service Line

from collections import deque

class Queue:

    def __init__(self):
        self.customers = deque()

    def enqueue(self, customer):
        """Add a new customer to the queue."""
        self.customers.append(customer)
        print(f"Customer added: {customer}")
    
    def dequeue(self):
        """Remove the next customer from the queue."""
        if not self.is_empty():
            customer = self.customers.popleft()
            print(f"Serving customer: {customer}")
            return customer
        raise IndexError("Error -> No customers in the queue.")
    
    def is_empty(self):
        return len(self.customers) == 0
    
    def print_queue(self):
        if self.is_empty():
            print("No customers in the queue.")
        else:
            print("Customers in queue:", list(self.customers))

def main():

    queue = Queue()

    while True:

        command = input("Enter 'join' to add customer, 'serve' to process, or 'exit' to quit: ").strip().lower()

        if command == 'join':
            customer_name = input("Enter customer name: ")
            queue.enqueue(customer_name)
            queue.print_queue()
        elif command == 'serve':
            try:
                queue.dequeue()
                queue.print_queue()
            except IndexError as e:
                print(e)
        elif command == 'exit':
            print("Exiting...")
            break
        else:
            print("Invalid command.")

if __name__ == '__main__':
    main()