# Node class for circular linked list
class CircularNode:
    def __init__(self, data):  # Correct constructor with double underscores
        self.data = data
        self.next = None

# Circular linked list class
class CircularLinkedList:
    def __init__(self):  # Correct constructor with double underscores
        self.head = None
        self.tail = None

    # Add a new node at the end
    def add(self, data):
        new_node = CircularNode(data)

        # If the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head  # Circular link
        else:
            self.tail.next = new_node  # Link last node to new node
            self.tail = new_node       # Update tail
            self.tail.next = self.head # Point tail back to head

    # Print the circular linked list
    def print_list(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        while True:
            print(temp.data, end=" → ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to start)")

# Test the circular linked list
if __name__ == "__main__":
    clist = CircularLinkedList()
    clist.add(1)
    clist.add(2)
    clist.add(3)
    clist.print_list()  # Expected output: 1 → 2 → 3 → (back to start)
