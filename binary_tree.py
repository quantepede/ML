class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""

        if self.preorder_search(self.root, find_val):
            return True
        else:
            return False


    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        traversal = []
        self.preorder_print(self.root, traversal)
        print("-".join(map(str,traversal)))

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        if start is None:
            return False
        elif start.value == find_val:
            return True
        elif self.preorder_search(start.left, find_val):
            return True
        elif self.preorder_search(start.right, find_val):
            return True
        else:
            return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""

        if start is not None:
            traversal.append(start.value)

        if start.left is not None:
            self.preorder_print(start.left, traversal)

        if start.right is not None:
            self.preorder_print(start.right, traversal)

        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.right.left = Node(6)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.right.left = Node(15)

# Test search
# Should be True
print(tree.search(1))
#
# Should be False
print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print(tree.print_tree())