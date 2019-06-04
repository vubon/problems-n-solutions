import unittest
from problem_03 import Node, lca


class LCATest(unittest.TestCase):

    def setUp(self) -> None:
        self.root = Node(1)
        self.node2 = self.root.left = Node(2)
        self.node5 = self.node2.right = Node(5)
        self.node4 = self.node2.left = Node(4)
        self.node8 = self.node4.left = Node(8)
        self.node9 = self.node4.right = Node(9)

        self.node3 = self.root.right = Node(3)
        self.node6 = self.node3.left = Node(6)
        self.node7 = self.node3.right = Node(7)

    def test_case_01(self):
        """
        LCA(Node(6), Node(7)) should return 3
        :return:
        """
        self.assertEqual(lca(self.node6, self.node7), 3)

    def test_case_02(self):
        """
        LCA(Node(3), Node(7)) should return 3
        :return:
        """
        self.assertEqual(lca(self.node3, self.node7), 3)

    def test_case_03(self):
        """
        When does not exists the value in the current nodes then return None
        :return:
        """
        self.assertEqual(lca(Node(77), Node(30)), None)


if __name__ == '__main__':
    unittest.main()
