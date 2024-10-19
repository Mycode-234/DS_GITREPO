class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

# Function to insert a node at the beginning of the list
def addAtBeginning(start_ref, new_data):
    # Create a new node
    new_node = Node(new_data)
    # Set current start node as the link to the new node
    new_node.link = start_ref
    # Return the new node as the start of the list
    return new_node

# Function to locate the middle node in the linked list
def locateMiddle(start):
    slow = start
    fast = start
    # Traverse the list to find the middle
    while fast and fast.link:
        slow = slow.link
        fast = fast.link.link
    return slow.data if slow else None

# Driver code
start = None
for num in range(8, 0, -1):
    start = addAtBeginning(start, num)
print("Middle element of the linked list:", locateMiddle(start))
