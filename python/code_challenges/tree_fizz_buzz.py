from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def fizz_buzz_tree(tree):
  if not tree:
    return None

  new_tree = KaryTree(TreeNode(None))
  proccess_node(tree.root, new_tree.root)

  return new_tree

def proccess_node(node, new_node):
  if node.value % 15 == 0:
    new_node.value = 'FizzBuzz'
  elif node.value % 5 == 0:
    new_node.value = 'Buzz'
  elif node.value % 3 == 0:
    new_node.value = 'Fizz'
  else:
    new_node.value = str(node.value)

  for child in node.children:
    new_child = TreeNode(None)
    new_node.children.append(new_child)
    proccess_node(child, new_child)

  return new_node
