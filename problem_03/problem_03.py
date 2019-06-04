# create Node
class Node:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return f"Node number: {self.value}"


root = Node(1)
node2 = root.left = Node(2)
node5 = node2.right = Node(5)
node4 = node2.left = Node(4)
node8 = node4.left = Node(8)
node9 = node4.right = Node(9)

node3 = root.right = Node(3)
node6 = node3.left = Node(6)
node7 = node3.right = Node(7)


def helper_function(root_node, one, two):
    """
    :param root_node:
    :param one:
    :param two:
    :return:
    """
    if root_node is None:
        return None

    if one == root_node.value or two == root_node.value:
        return root_node

    # Finding the value in left side and right side
    left_subtree = helper_function(root_node.left, one, two)
    right_subtree = helper_function(root_node.right, one, two)

    if left_subtree and right_subtree:
        return root_node

    return left_subtree if left_subtree is not None else right_subtree


def lca(node_one, node_two):
    """
    :param node_one:
    :param node_two:
    :return:
    """
    return helper_function(root, node_one.value, node_two.value)


print(lca(Node(3), Node(7)).value)
