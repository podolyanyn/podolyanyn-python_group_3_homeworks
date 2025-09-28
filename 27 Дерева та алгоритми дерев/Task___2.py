from bs4 import BeautifulSoup
import os
class Node:
    def __init__(self, tag, text="", attrs=None):
        self.tag = tag
        self.text = text.strip() if text else ""
        self.attrs = attrs or {}
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __repr__(self):
        return f"<{self.tag} {self.attrs}> {self.text}"


def build_tree(soup_element):
    if getattr(soup_element, "name", None) is None:
        return None
    node_text = soup_element.get_text(strip=True) if soup_element.string else ""
    node = Node(soup_element.name, node_text, dict(getattr(soup_element, "attrs", {})))
    for child in getattr(soup_element, "children", []):
        child_node = build_tree(child)
        if child_node:
            node.add_child(child_node)
    return node

def search_by_tag(node, tag):
    results = []
    if node.tag == tag and node.text:
        results.append(node.text)
    for child in node.children:
        results.extend(search_by_tag(child, tag))
    return results

def search_by_attr(node, attr_name, attr_value):
    results = []
    if node.attrs.get(attr_name) == attr_value and node.text:
        results.append(node.text)
    for child in node.children:
        results.extend(search_by_attr(child, attr_name, attr_value))
    return results

def print_tree(node, level=0):
    indent = "  " * level
    print(f"{indent}<{node.tag} {node.attrs}> {node.text}")
    for child in node.children:
        print_tree(child, level + 1)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, "lesson_tree_hw.html")

    if not os.path.exists(path):
        print(" Файл не знайдено:", path)
        print(" Файли у папці скрипта:")
        try:
            for name in os.listdir(script_dir):
                print("  -", name)
        except Exception as e:
            print("Не вдалося перерахувати файли:", e)
        raise SystemExit(0)

    with open(path, encoding="windows-1251") as f:
        html_doc = f.read()
    print(" Файл знайдено і прочитано успішно!\n")

    soup = BeautifulSoup(html_doc, "html.parser")
    if soup.html is None:
        print("Не знайшов <html> у документі.")
        raise SystemExit(0)

    dom_tree = build_tree(soup.html)

    print(" Структура DOM-дерева:")
    print_tree(dom_tree)

    print("\n Тексти в <h2>:")
    print(search_by_tag(dom_tree, "h2"))

    print("\n Тексти в <div id='content'>:")
    print(search_by_attr(dom_tree, "id", "content"))