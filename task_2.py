class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert_into_tree(root, key):
    if root is None:
        return TreeNode(key)

    if key < root.key:
        root.left = insert_into_tree(root.left, key)
    elif key > root.key:
        root.right = insert_into_tree(root.right, key)

    return root


def find_min_value(root):
    if root is None:
        return None

    while root.left:
        root = root.left

    return root.key


array = [1, 5, 7, 10, 38, 4, 15]
root = None

for value in array:
    root = insert_into_tree(root, value)

min_value = find_min_value(root)

print("Дерево з масиву:", array)
print("Найменше значення в дереві:", min_value)
