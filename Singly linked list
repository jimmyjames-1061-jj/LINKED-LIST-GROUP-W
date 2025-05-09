class Node:
    def __init__(self, data):
        # Stores data in the node
        self.data = data
        # Reference to the next node in the list
        self.next = None


def insert_at_beginning(head, data):
   # Inserts a new node with the given data at the beginning of the list.
  
    new_node = Node(data)
    new_node.next = head  # Point the new node's next to the current head
    return new_node  # The new node becomes the new head


def traverse(head):
   # Traverses the linked list and prints each node's data.

    current = head
    while current:
        # Print current node's data followed by an arrow
        print(str(current.data) + "->", end="")
        current = current.next
    # Print None to indicate the end of the list
    print("None")


def insert_after_node(node, data):
    # Inserts a new node after the specified node in the list.
   
    if node is None:
        print("Error: The node given is None")
        return
    # Create a new node and link it to the node after the specified node
    new_node = Node(data)
    new_node.next = node.next
    node.next = new_node


def insert_at_end(head, data):
    #Inserts a new node at the end of the list.
    new_node = Node(data)
    # If the list is empty, the new node becomes the head
    if head is None:
        return new_node

    # Traverse to the last node
    current = head
    while current.next:
        current = current.next
    # Append the new node
    current.next = new_node
    return head


# Initialize an empty linked list
head = None

# Insert nodes at the beginning
head = insert_at_beginning(head, 4)
head = insert_at_beginning(head, 3)
head = insert_at_beginning(head, 2)
head = insert_at_beginning(head, 1)

# Inserts 1.5 after the first node (which contains 1)
insert_after_node(head, 1.5)

# Inserts 5 at the end of the list
head = insert_at_end(head, 5)

# Traverse the list and print its content
traverse(head)
