class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):

        self.insert_binary_search_tree(self.root, new_val)


    def search(self, find_val):
        if self.binary_search_tree(self.root, find_val):
            return True
        else:
            return False


    def insert_binary_search_tree(self, current, new_val):

        if current:
            if new_val < current.value:
                if not current.left:
                    current.left = Node(new_val)
                else:
                    self.insert_binary_search_tree(current.left, new_val)
            if new_val > current.value:
                if not current.right:
                    current.right = Node(new_val)
                else:
                    self.insert_binary_search_tree(current.right, new_val)

        # else:
        #     current = Node(new_val)

    def binary_search_tree(self, start, find_val):
        if start is None:
            return False
        elif start.value == find_val:
            return True
        elif find_val > start.value:
            self.binary_search_tree(start.right, find_val)
        elif find_val < start.value:
            self.binary_search_tree(start.left, find_val)
        else:
            return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        traversal = []
        self.preorder_print(self.root, traversal)
        print("-".join(map(str,traversal)))

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
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)


# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(2))

print(tree.print_tree())
