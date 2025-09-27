class Tree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None
        self.subtree = None

    def add_left(self,data):
        if self.left is None:
            self.left = Tree(data)

        else:
            temperory_left = Tree(data)
            temperory_left.left = self.left
            self.left = temperory_left

    def add_right(self,data):
        if self.right is None:
            self.right = Tree(data)

        else:
            temperory_right = Tree(data)
            temperory_right.right = self.right
            self.right = temperory_right

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def __str__(self):
        return str(self.root)

    def preorder(self):
        print(self)
        if self.get_left():
            self.get_left().preorder()
        if self.get_right():
            self.get_right().preorder()

    def insert_subtree_left(self, subtree):
        if not isinstance(subtree, Tree):
            raise TypeError("Очікується об'єкт типу Tree")
        subtree.left = self.left
        self.left = subtree

    def insert_subtree_right(self, subtree):
        if not isinstance(subtree, Tree):
            raise TypeError("Очікується об'єкт типу Tree")
        subtree.right = self.right
        self.right = subtree

    def remove_left_subtree(self):
        self.left = None

    def remove_right_subtree(self):
        self.right = None


my_tree = Tree(100)
my_tree.add_left(50)
my_tree.add_right(150)
my_tree.add_left(75)
my_tree.add_right(175)

subtree = Tree(999)
subtree.add_left(998)
subtree.add_right(1001)

my_tree.insert_subtree_left(subtree)
my_tree.remove_right_subtree()

# print(my_tree)
# print(my_tree.root,my_tree.left.root,my_tree.left.left.root,my_tree.right.root)

# print(my_tree.get_left())
# print(my_tree.get_left().get_left())
my_tree.get_left().add_right(51)
my_tree.get_right().add_left(149)

# print(my_tree)

def preorder(tree):
    if tree:
        print(tree)
        preorder(tree.get_left())
        preorder(tree.get_right())

# preorder(my_tree)
# 100 75 50 51 175 149 150
my_tree.preorder()

def postorder(tree):
    if tree:
        postorder(tree.get_left())
        postorder(tree.get_right())
        print(tree)
# 50 51 75 149 150 175 100
# postorder(my_tree)

def inorder(tree):
    if tree:
        inorder(tree.get_left())
        print(tree)
        inorder(tree.get_right())
# 50 75 51 100 149 175 150
# inorder(my_tree)

def printexp(tree):
  sVal = ""
  if tree:
      sVal = '(' + printexp(tree.get_left())
      sVal = sVal + str(tree)
      sVal = sVal + printexp(tree.get_right())+')'
  return sVal

# print(printexp(my_tree))

