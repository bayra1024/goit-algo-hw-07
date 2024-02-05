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


def find_max_value(root):
    # Якщо дерево порожнє, повертаємо None
    if root is None:
        return None

    # Якщо існує правий вузол, максимальне значення знаходиться в ньому
    while root.right:
        root = root.right

    return root.key


# Створення дерева з масиву
array = [1, 5, 7, 10, 38, 4, 15]
root = None

for value in array:
    root = insert_into_tree(root, value)

# Знаходження найбільшого значення в дереві
max_value = find_max_value(root)
print("Дерево з масиву:", array)
print("Найбільше значення в дереві:", max_value)
