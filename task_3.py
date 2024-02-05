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


def tree_sum(root):
    if root is None:
        return 0

    return root.key + tree_sum(root.left) + tree_sum(root.right)


# Створення дерева з масиву
array = [1, 5, 7, 10, 38, 4, 15]
root = None

for value in array:
    root = insert_into_tree(root, value)

# Знаходження суми всіх значень в дереві
total_sum = tree_sum(root)
print("Дерево з масиву:", array)
print("Сума всіх значень в дереві:", total_sum)
