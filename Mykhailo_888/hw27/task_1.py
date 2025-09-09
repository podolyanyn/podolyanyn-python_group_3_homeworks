class Tree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def add_left(self, data):
        if self.left_child is None:
            self.left_child = Tree(data)
        else:
            temp = Tree(data)
            temp.left_child = self.left_child
            self.left_child = temp

    def add_right(self, data):
        if self.right_child is None:
            self.right_child = Tree(data)
        else:
            temp = Tree(data)
            temp.right_child = self.right_child
            self.right_child = temp

    def replace_left_subtree(self, new_tree):
        self.left_child = new_tree

    def replace_right_subtree(self, new_tree):
        self.right_child = new_tree

    def detach_left(self):
        detached = self.left_child
        self.left_child = None
        return detached

    def detach_right(self):
        detached = self.right_child
        self.right_child = None
        return detached

    def get_left(self):
        return self.left_child

    def get_right(self):
        return self.right_child

    def __str__(self):
        return str(self.value)

    def preorder(self):
        result = [self.value]
        if self.left_child:
            result += self.left_child.preorder()
        if self.right_child:
            result += self.right_child.preorder()
        return result

root = Tree(200)
root.add_left(60)
root.add_right(150)

L = Tree(10)
L.add_left(6)
L.add_right(15)

R = Tree(100)
R.add_left(180)
R.add_right(225)

root.replace_left_subtree(L)
root.replace_right_subtree(R)

print("Після замін:", root.preorder())

det = root.detach_left()
print("Після detach_left:", root.preorder())
print("Від’єднане піддерево:", det.preorder() if det else None)