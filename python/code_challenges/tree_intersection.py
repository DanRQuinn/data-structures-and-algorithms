from data_structures.binary_tree import BinaryTree


def tree_intersection(tree_a, tree_b):
  # create a set to store the values found in both trees
  set_of_values = set()
  # create a hashmap to store the values of tree_a
  hashmap = {}
  # traverse tree_a and add the values to the hashmap
  def traverse_a(node):
    if node:
      # add the value to the hashmap
      hashmap[node.value] = node.value
      # traverse the left and right nodes
      traverse_a(node.left)
      traverse_a(node.right)
  traverse_a(tree_a.root)
  # traverse tree_b and check if the value is in the hashmap
  def traverse_b(node):
    if node:
      if node.value in hashmap:
        # if the value is in the hashmap, add it to the set
        set_of_values.add(node.value)
      traverse_b(node.left)
      traverse_b(node.right)
  traverse_b(tree_b.root)
  # return the set of values
  return set_of_values
