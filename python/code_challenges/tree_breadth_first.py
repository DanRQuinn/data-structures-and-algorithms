from data_structures.binary_tree import BinaryTree


def breadth_first(tree):
    if not tree.root:
        return []

    queue = [tree.root]
    values = []

    while queue:
        node = queue.pop(0)
        values.append(node.value)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return values
