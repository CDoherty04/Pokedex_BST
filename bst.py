from binarynode import BinaryNode


def _find_max(node):
    current = node
    # loop down to rightmost leaf
    while current.right is not None:
        current = current.right
    return current


class BST:

    def __init__(self):
        self._root = None

    def add(self, entry):
        """Adds an object to the BST by creating smaller and larger subtrees"""

        new_node = BinaryNode(entry)
        if self._root is None:
            self._root = new_node

        else:
            self._rec_add(new_node, self._root)

    def _rec_add(self, new_node, cur_node):
        """Recursively adds downstream"""

        # Check left
        if new_node.entry < cur_node.entry:
            if cur_node.left is None:
                cur_node.left = new_node
            else:
                self._rec_add(new_node, cur_node.left)

        # Check right
        elif new_node.entry > cur_node.entry:
            if cur_node.right is None:
                cur_node.right = new_node
            else:
                self._rec_add(new_node, cur_node.right)

        else:
            raise ValueError

    def search(self, key):
        """Searches the BST for a key"""

        if self._root is None:
            raise KeyError

        return self._rec_search(key, self._root)

    def _rec_search(self, key, cur_node):
        """Recursively searches downstream"""

        if cur_node.entry == key:
            return cur_node.entry
        elif cur_node.entry < key:
            self._rec_search(key, cur_node.left)
        elif cur_node.entry > key:
            self._rec_search(key, cur_node.right)
        else:
            raise KeyError

    def preorder(self, visit_function):
        """Prints the tree based on preorder"""

        return self._rec_preorder(visit_function, self._root)

    def _rec_preorder(self, visit_function, cur_node):
        # Return Nothing if the tree is empty
        if cur_node is None:
            return None

        # Calls visit function on the current node's entry
        visit_function(cur_node.entry)

        # Traverse left
        self._rec_preorder(visit_function, cur_node.left)

        # Traverse right
        self._rec_preorder(visit_function, cur_node.right)

    def inorder(self, visit_function):
        """Prints the tree based on inorder"""

        return self._rec_inorder(visit_function, self._root)

    def _rec_inorder(self, visit_function, cur_node):
        # Return Nothing if the tree is empty
        if cur_node is None:
            return None

        # Traverse left
        self._rec_inorder(visit_function, cur_node.left)

        # Calls visit function on the current node's entry
        visit_function(cur_node.entry)

        # Traverse right
        self._rec_inorder(visit_function, cur_node.right)

    def postorder(self, visit_function):
        """Prints the tree based on postorder"""

        return self._rec_postorder(visit_function, self._root)

    def _rec_postorder(self, visit_function, cur_node):
        # Return Nothing if the tree is empty
        if cur_node is None:
            return None

        # Traverse left
        self._rec_postorder(visit_function, cur_node.left)

        # Traverse right
        self._rec_postorder(visit_function, cur_node.right)

        # Calls visit function on the current node's entry
        visit_function(cur_node.entry)

    def remove(self, key):
        """Removes the target node from the BST"""

        self._root = self._rec_remove(self._root, key)

    def _rec_remove(self, root, key):
        if root is None:
            return root

        # If the key is less than the root's id
        if key < root.entry.id:
            root.left = self._rec_remove(root.left, key)

        # If the key is greater than the root's id
        elif key > root.entry.id:
            root.right = self._rec_remove(root.right, key)

        # If the key is found
        else:
            # Node with one or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children
            # Get maximum value node (largest in the left subtree)
            temp = _find_max(root.left)

            # Copy the maximum value node's id to the current node
            root.id = temp.entry.id

            # Delete the maximum value node
            root.left = self._rec_remove(root.left, temp.entry.id)

        return root

    def copy(self):
        if self._root is None:
            return None  # Empty tree
        return self._rec_copy(self._root)

    def _rec_copy(self, cur_node):
        # Create a new node with the same entry.id
        new_node = BinaryNode(cur_node.entry.id)

        # Recursively copy the left and right subtrees
        new_node.left = self._rec_copy(cur_node.left)
        new_node.right = self._rec_copy(cur_node.right)

        return new_node