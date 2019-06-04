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


def helper_function(root_node, node_1, node_2):
    """
    :param root_node:
    :param node_1:
    :param node_2:
    :return:
    """
    if root_node is None:
        return None

    if node_1 == root_node.value or node_2 == root_node.value:
        return root_node

    # Finding the value in left side and right side
    left_subtree = helper_function(root_node.left, node_1, node_2)
    right_subtree = helper_function(root_node.right, node_1, node_2)

    # if the nodes value are existing both sides then LCA must be Root Node
    if left_subtree and right_subtree:
        return root_node

    # checking not left_subtree is not None then the LCA must be exists in left tree else right sub tree
    return left_subtree if left_subtree is not None else right_subtree


def lca(node_one, node_two):
    """
    Time Complexity is O(n) and Space complexity also O(n). Because both complexity are depending on N.
    :param node_one:
    :param node_two:
    :return:
    """
    result = helper_function(root, node_one.value, node_two.value)
    if result is None:
        return None
    return result.value


# ==================== Examples =============================== #
# when you will run the test case , please comment out  below line

# print("LCA of 3 & 7 is", lca(Node(3), Node(7)))
# print("LCA of 7 & 9 is", lca(Node(7), Node(9)))
# print("LCA of 6 & 7 is", lca(Node(6), Node(7)))
# print("LCA of 8 & 9 is", lca(Node(8), Node(9)))
# print("LCA of 4 & 5 is", lca(Node(4), Node(5)))
# print("LCA of 4 & 2 is", lca(Node(4), Node(2)))
# print("LCA of 11 & 10 is", lca(Node(11), Node(10)))
