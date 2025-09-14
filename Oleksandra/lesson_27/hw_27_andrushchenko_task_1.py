class Tree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    # --- Додавання вузлів ---
    def add_left(self, data):
        """Додає новий лівий вузол. Якщо вузол вже існує — попереджає."""
        if self.left is None:
            self.left = Tree(data)
        else:
            print("Лівий вузол уже існує. Вставка не виконана.")

    def add_right(self, data):
        """Додає новий правий вузол. Якщо вузол вже існує — попереджає."""
        if self.right is None:
            self.right = Tree(data)
        else:
            print("Правий вузол уже існує. Вставка не виконана.")

    # --- Пошук вузла та його батька ---
    def find_node_and_parent(self, value, parent=None):
        if self.root == value:
            return self, parent

        if self.left:
            node, par = self.left.find_node_and_parent(value, self)
            if node:
                return node, par

        if self.right:
            node, par = self.right.find_node_and_parent(value, self)
            if node:
                return node, par

        return None, None

    # --- Вставка піддерева ---
    def insert_subtree(self, target_value, new_tree, side="left"):
        target_node, _ = self.find_node_and_parent(target_value)
        if not target_node:
            print(f"Помилка: Вузол зі значенням {target_value} не знайдено.")
            return

        if side == "left":
            if target_node.left:
                print(f"УВАГА: Лівий нащадок вузла {target_value} буде замінений.")
            target_node.left = new_tree
        elif side == "right":
            if target_node.right:
                print(f"УВАГА: Правий нащадок вузла {target_value} буде замінений.")
            target_node.right = new_tree
        else:
            print("Помилка: side має бути 'left' або 'right'.")

    # --- Видалення піддерева ---
    def delete_subtree(self, target_value):
        # Видалення всього дерева
        if self.root == target_value:
            self.root = None
            self.left = None
            self.right = None
            print("Все дерево було очищено.")
            return

        target_node, parent = self.find_node_and_parent(target_value)
        if not target_node:
            print(f"Помилка: Вузол зі значенням {target_value} не знайдено.")
            return

        if parent.left and parent.left.root == target_value:
            parent.left = None
        elif parent.right and parent.right.root == target_value:
            parent.right = None
        print(f"Піддерево з коренем {target_value} видалено.")

# --- Виведення дерева ---
def print_tree_structure(tree, level=0, prefix="Root: "):
    if tree and tree.root is not None:
        print(" " * (level * 4) + prefix + str(tree.root))
        print_tree_structure(tree.left, level + 1, "L-- ")
        print_tree_structure(tree.right, level + 1, "R-- ")

# --- Тестування ---
if __name__ == "__main__":
    my_tree = Tree(100)
    my_tree.add_left(50)
    my_tree.add_right(150)

    print("Початкове дерево:")
    print_tree_structure(my_tree)
    print("-----------------------------------")

    new_sub_tree = Tree(200)
    new_sub_tree.add_left(190)
    new_sub_tree.add_right(210)

    my_tree.insert_subtree(150, new_sub_tree, side="left")

    print("\nДерево після вставки піддерева:")
    print_tree_structure(my_tree)
    print("-----------------------------------")

    my_tree.delete_subtree(50)
    print("\nДерево після видалення піддерева 50:")
    print_tree_structure(my_tree)
