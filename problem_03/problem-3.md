3) Write following functions body. 2 Nodes are passed as parameter. You need to find Least Common Ancestor and print its value. Node structure are as following:

![Node Image](https://github.com/vubon/problems-n-solutions/blob/master/problem_03/node_tree.png?raw=true)

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

```

## Ancestor Definition: 
1. Any node falls under parent chain till root node.
2. A node is an ancestor of itself.

**For example:** if we consider Node 7 it’s ancestors will be 1, 3, and 7.

All nodes values are unique for this tree.

You function needs to find least common ancestor (closest common ancestor).

#### For an example for the tree image, 
1. If 6 and 7 passed to lca it should return 3
2. If 3 and 7 passed to lca it should return 3

```python
def lca(node1, node2):
    """
    :param: node1
    :param: node2
    """
    # Write function body

```

<p>You may write additional function.<br/>
Explain the Runtime and Memory requirements for your solution.</p>
