from binarynode import BinaryNode


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

        if self._root is None:
            raise KeyError

        return self._rec_search(key, self._root)

    def _rec_remove(self, key, cur_node):
        """Recursively searches downstream until it finds the target and removes it"""

        if cur_node.entry == key:
            # Figure out how to update parent node
            temp = cur_node
