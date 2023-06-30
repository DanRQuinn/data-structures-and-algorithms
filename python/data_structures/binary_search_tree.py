from data_structures.binary_tree import BinaryTree
from data_structures.binary_tree import Node


class BinarySearchTree(BinaryTree):
    """
    This class represents a binary search tree.

    Attributes:
        root: The root node of the tree.
    """

    def __init__(self, root=None):
        """
        Initialize the binary search tree.

        Args:
            root: The root node of the tree.
        """
        self.root = root

    def add(self, value):
        """
        Add a new node to the tree with the given value.

        Args:
            value: The value of the new node.
        """
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        return
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        return
                    else:
                        current_node = current_node.right
        return self.root

    def contains(self, value):
        """
        Check if the tree contains a node with the given value.

        Args:
            value: The value to check for.

        Returns:
            True if the tree contains a node with the given value, False otherwise.
        """
        current_node = self.root
        while current_node is not None:
            if value == current_node.value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False
