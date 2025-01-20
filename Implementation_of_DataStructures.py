# Node class for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def delete_at_end(self):
        if not self.head:
            print("List is empty.")
            return
        if not self.head.next:
            self.head = None
        else:
            temp = self.head
            while temp.next and temp.next.next:
                temp = temp.next
            temp.next = None

    def display(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Stack class
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.stack:
            print("Stack is empty.")
        else:
            print("Popped:", self.stack.pop())

    def display(self):
        if not self.stack:
            print("Stack is empty.")
        else:
            print("Stack:", self.stack)

# Queue class
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.queue:
            print("Queue is empty.")
        else:
            print("Dequeued:", self.queue.pop(0))

    def display(self):
        if not self.queue:
            print("Queue is empty.")
        else:
            print("Queue:", self.queue)

# Main function
def main():
    linked_list = LinkedList()
    stack = Stack()
    queue = Queue()

    while True:
        print("\nMenu:")
        print("1. Linked List Operations")
        print("2. Stack Operations")
        print("3. Queue Operations")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\nLinked List Operations:")
            print("1. Insert at end")
            print("2. Delete from end")
            print("3. Display linked list")
            l_choice = int(input("Enter your choice: "))
            
            if l_choice == 1:
                data = int(input("Enter data to insert: "))
                linked_list.insert_at_end(data)
            elif l_choice == 2:
                linked_list.delete_at_end()
            elif l_choice == 3:
                linked_list.display()
            else:
                print("Invalid choice.")
        
        elif choice == 2:
            print("\nStack Operations:")
            print("1. Push")
            print("2. Pop")
            print("3. Display stack")
            s_choice = int(input("Enter your choice: "))
            
            if s_choice == 1:
                data = int(input("Enter data to push: "))
                stack.push(data)
            elif s_choice == 2:
                stack.pop()
            elif s_choice == 3:
                stack.display()
            else:
                print("Invalid choice.")
        
        elif choice == 3:
            print("\nQueue Operations:")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Display queue")
            q_choice = int(input("Enter your choice: "))
            
            if q_choice == 1:
                data = int(input("Enter data to enqueue: "))
                queue.enqueue(data)
            elif q_choice == 2:
                queue.dequeue()
            elif q_choice == 3:
                queue.display()
            else:
                print("Invalid choice.")
        
        elif choice == 4:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
