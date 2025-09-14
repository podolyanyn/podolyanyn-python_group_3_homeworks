class Tree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

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

    def add_tree_right(self,exsemplyar):
        if self.right is None:
            self.right = exsemplyar

        else:
            temperory = self.right
            self.right = exsemplyar
            if temperory.root < exsemplyar.left.root:
                exsemplyar.left.left = temperory
            elif exsemplyar.left.root < temperory.root < exsemplyar.right.root and exsemplyar.right.root - temperory.root>=50:
                exsemplyar.left.right = temperory
            elif exsemplyar.left.root < temperory.root < exsemplyar.right.root and exsemplyar.right.root - temperory.root<50:
                exsemplyar.right.left = temperory
            elif temperory.root > exsemplyar.right.root:
                exsemplyar.right.right = temperory

    def add_tree_left(self,exsemplyar):
        if self.left is None:
            self.left = exsemplyar
        else:
            temperory = self.left
            self.left = exsemplyar
            if temperory.root < exsemplyar.left.root:
                exsemplyar.left.left = temperory
            elif exsemplyar.left.root < temperory.root < exsemplyar.right.root and exsemplyar.right.root - temperory.root >= 50:
                exsemplyar.left.right = temperory
            elif exsemplyar.left.root < temperory.root < exsemplyar.right.root and exsemplyar.right.root - temperory.root < 50:
                exsemplyar.right.left = temperory
            elif temperory.root > exsemplyar.right.root:
                exsemplyar.right.right = temperory




    def add_tree(self,exsemplyar):
        if exsemplyar.root < self.root:
            if self.left is None:
                self.left = exsemplyar
            else:
                temperory = self.left
                self.left = exsemplyar
                if temperory.root < exsemplyar.left.root:
                    exsemplyar.left.left = temperory
                elif exsemplyar.left.root < temperory.root < exsemplyar.right.root and exsemplyar.right.root - temperory.root >= 50:
                    exsemplyar.left.right = temperory
                elif exsemplyar.left.root < temperory.root < exsemplyar.right.root and exsemplyar.right.root - temperory.root < 50:
                    exsemplyar.right.left = temperory
                elif temperory.root > exsemplyar.right.root:
                    exsemplyar.right.right = temperory

        elif exsemplyar.root > self.root:
            if self.right is None:
                self.right = exsemplyar

            else:
                temperory = self.right
                self.right = exsemplyar
                if temperory.root < exsemplyar.left.root:
                    exsemplyar.left.left = temperory
                elif exsemplyar.left.root < temperory.root < exsemplyar.right.root and exsemplyar.right.root - temperory.root >= 50:
                    exsemplyar.left.right = temperory
                elif exsemplyar.left.root < temperory.root < exsemplyar.right.root and exsemplyar.right.root - temperory.root < 50:
                    exsemplyar.right.left = temperory
                elif temperory.root > exsemplyar.right.root:
                    exsemplyar.right.right = temperory

    def add_subtree_at(self,new_tree,direction):
        if direction == 'left':
            if self.left is None:
                self.left = new_tree
            else:
                temp = self.left
                self.left = new_tree
                if new_tree.left is None and new_tree.right is None:
                    new_tree.left = temp
                else:
                    new_tree.find_and_relink(temp)

        elif direction == 'right':
            if self.right is None:
                self.right = new_tree
            else:
                temp = self.right
                self.right = new_tree
                if new_tree.left is None and new_tree.right is None:
                    new_tree.right = temp
                else:
                    new_tree.find_and_relink(temp)

        else:
            print('Invalid direction, please enter either left or right')


    def find_and_relink(self,node_to_relink):
        if node_to_relink.root < self.root:
            if self.left  == None:
                self.left = node_to_relink
            else:
                self.left.find_and_relink(node_to_relink)

        elif node_to_relink.root > self.root:
            if self.right == None:
                self.right = node_to_relink
            else:
                self.right.find_and_relink(node_to_relink)

def printexp(tree):
    try:
        sVal = ''
        if tree :
            sVal = '('+ printexp(tree.get_left())
            sVal = sVal + str(tree)
            sVal = sVal + printexp(tree.get_right()) + ')'
        return sVal
    except:AttributeError

def inorder(tree):
    if tree :
        inorder(tree.get_left())
        print(printexp(tree))
        inorder(tree.get_right())




my_tree = Tree(500)
my_tree.add_left(300)
my_tree.add_right(600)
my_tree.left.add_left(50)
my_tree.left.add_right(250)
my_tree.right.add_right(1800)
my_tree.right.add_left(1100)

my_tree2 = Tree(200)
my_tree2.add_left(150)
my_tree2.add_right(180)
my_tree2.left.add_left(100)
my_tree2.left.add_right(120)
my_tree2.right.add_right(160)
my_tree2.right.add_left(170)
my_tree3 = Tree(1600)

print(printexp(my_tree))
print(printexp(my_tree2))
my_tree.left.add_subtree_at(my_tree2,'left')
print(printexp(my_tree))
my_tree.right.add_subtree_at(my_tree3,'right')
print(printexp(my_tree))

"""Всі методи зробив сам окрім add_subtree_at і find_and_relink . Для них довелося використовувати Джеміні ШІ в якості ментора ,який 
давав покрокові підказки як робити. Методи add_tree_righ,add_tree_left,add_tree теж додають дерево в середину іншого дерева,
але за умови що дерево яке додається має лише корінь і лише 2 нащадки, а ті в свою чергу не мають своїх нащадків(тобто трикутничок такий)
"""