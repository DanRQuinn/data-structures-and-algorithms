from data_structures.invalid_operation_error import InvalidOperationError

# A stack is a data structure that follows the last in, first out (LIFO) principle.

class Node:

    # The constructor initializes a node with the given value.
    # The `next` parameter is optional, and defaults to None.

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:

    # The constructor initializes the stack with the given node.
    # The default value of the node parameter is None, which creates an empty stack.

    def __init__(self, node=None):
        self.top = node

    # The push method adds a new node to the top of the stack.

    def push(self, value):
        # Create a new node with the given value.
        new_node = Node(value)
        # Set the new node's next pointer to the current top of the stack.
        new_node.next = self.top
        # Set the top of the stack to the new node.
        self.top = new_node

    # The pop method removes the top node from the stack.

    def pop(self):
        # If the stack is empty, raise an exception.
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        # Save the value of the top node.
        value = self.top.value
        # Set the top of the stack to the next node.
        self.top = self.top.next
        return value

    # The peek method returns the value of the top node, without removing it.

    def peek(self):
        # If the stack is empty, raise an exception.
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    # The is_empty method returns True if the stack is empty, and False otherwise.

    def is_empty(self):
        return self.top is None

