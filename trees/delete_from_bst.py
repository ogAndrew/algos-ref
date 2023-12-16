"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def delete_from_bst_helper(root, key):
    if root is None:
        return root

    # Searching for a node with the given value.
    if key < root.value:
        root.left = delete_from_bst_helper(root.left, key)
    elif key > root.value:
        root.right = delete_from_bst_helper(root.right, key)
    else:
        # If the node to be deleted is a leaf node, replace it with None.
        if root.left is None and root.right is None:
            return None

        # If the node to be deleted has only one child, replace it with its non-None child.
        if root.left is None:
            temp = root.right
            return temp
        if root.right is None:
            temp = root.left
            return temp

        # If the node to be deleted has two child nodes, replace its value with that of its
        # inorder successor and recursively delete the inorder successor.
        temp = root.right
        while temp.left is not None:
            temp = temp.left
        root.value = temp.value
        root.right = delete_from_bst_helper(root.right, temp.value)

    return root

def delete_from_bst(root, values_to_be_deleted):
    if root is None or len(values_to_be_deleted) == 0:
        return root

    for key in values_to_be_deleted:
        root = delete_from_bst_helper(root, key)

    return root
