
#============================================================= 1 =======================================================
"""Розширити структуру, яку побудували на уроці, можливістю вставки дерева в наявне дерево та видалення піддерева з дерева, що існує."""

class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_left(self,data):
        if self.left is None:
            self.left = Tree(data)

        else:
            temporary_left = Tree(data)
            temporary_left.left = self.left
            self.left = temporary_left

    def add_right(self,data):
        if self.right is None:
            self.right = Tree(data)

        else:
            temporary_right = Tree(data)
            temporary_right.right = self.right
            self.right = temporary_right

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_last_left(self):
        if not self.get_left():
            return self
        return self.get_left().get_last_left()

    def insert_tree(self, new_tree, position_value):
        """ ADDING new tree
        replaced tree will be added to the most left node of new tree"""
        if self.left and self.left.value == position_value:
            temporary_tree = self.left
            self.left = new_tree
            self.left.get_last_left().left = temporary_tree
            return
        elif self.right and self.right.value == position_value:
            temporary_tree = self.right
            self.right = new_tree
            self.right.get_last_left().left = temporary_tree
            return
        if self.left:
            self.left.insert_tree(new_tree, position_value)
        if self.right:
            self.right.insert_tree(new_tree, position_value)

    def delete_tree(self, value):
        if self.left and self.left.value == value:
            self.left = None
            return True
        if self.right and self.right.value == value:
            self.right = None
            return True
        if self.left and self.left.delete_tree(value):
            return True
        if self.right and self.right.delete_tree(value):
            return True

        return False

    def __str__(self):
        return str(self.value)
#=============================================================== 2 AI used ====================================================
from bs4 import BeautifulSoup, NavigableString, Doctype, Comment

class PolyTree:
    def __init__(self, tag, text):
        self.tag = tag
        self.text = text
        self.children = []
        self.parent = None

    # Додаємо дитину
    def add_child(self, node):
        self.children.append(node)

    # Видаляємо дитину за значенням
    def remove_child(self, value):
        self.children = [child for child in self.children if child.value != value]

    # Пошук вузла за значенням (DFS)
    def find(self, value):
        if self.value == value:
            return self
        for child in self.children:
            result = child.find(value)
            if result:
                return result
        return None

    def print_tree(self, level=0):
        indent = " " * (level * 4)
        if self.text:
            print(f"{indent}<{self.tag}>: {self.text}")
        else:
            print(f"{indent}<{self.tag}>")
        for child in self.children:
            child.print_tree(level + 1)



html_fragment = """<!DOCTYPE HTML PUBLIC «-//W3C//DTD HTML 4.01 Transitional//EN» «http://www.w3.org/TR/html4/loose.dtd»>
<html>
    <head>
        <meta http–equiv= "Content–Type" content= text/html; charset=windows-1251″> <title> Домашнє завдання. Парсинг DOM і сбереження в дереві.</title>
    </head>
    <body>
        <table width= "805" border= "0" align="center" cellpadding="0" cellspacing="0" bgcolor="#ffff00">
            <tr>
                <td height ="190" colspan="3"align="center"><h2>Верхня частина-Header</h2></td>
            </tr>
            <tr>
                <td colspan="3"> <!-- --> 
                    <table width= "805" border= "0" align="center" cellpadding= "0" cellspacing="0" bgcolor="#ff0000">
                        <tr>
                            <td height ="40" align="center"><h2>Горизонтальний блок навігації</h2></td>
                        </tr>
                    </table>
                </td>
            </tr>
            <tr>
                <td width="230" valign="top" bgcolor="#d8cba8">
                    <div id ="col_left" align="center" > <h2>Ліва колонка</h2></div>
                </td>
                <td width="345" valign="top" bgcolor="#d8cba8">
                    <div id ="content" align="center" > <h2>Центральна частина</h2></div>
                </td>
                <td width="230" valign="top" bgcolor="#d8cba8">
                    <div id ="col_right" align="center" > <h2>Права колонка</h2></div>
                </td>
            </tr>
            <tr>
                <td colspan="3"align="center" bgcolor="#00ff00"><h2>Нижня частина-Footer</h2></td>
            </tr>
        </table>
    </body>
</html>"""

soup = BeautifulSoup(html_fragment, 'html.parser')

def build_DOM_tree(soup_node):
    # Ігноруємо Doctype та коментарі
    if isinstance(soup_node, (Doctype, Comment)):
        return None

    # Якщо це текст
    text = ''
    if isinstance(soup_node, NavigableString):
        text = soup_node.strip()
        if not text:  # пропускаємо пусті тексти
            return None

    new_node = PolyTree(
        tag=soup_node.name if soup_node.name else 'text',
        text=text
    )

    for child in getattr(soup_node, 'children', []):  # безпечний доступ до children
        child_node = build_DOM_tree(child)
        if child_node:  # ігноруємо None
            child_node.parent = new_node
            new_node.children.append(child_node)

    return new_node

DOM_object = build_DOM_tree(soup)
DOM_object.print_tree()