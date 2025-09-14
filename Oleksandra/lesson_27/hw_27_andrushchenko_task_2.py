from html.parser import HTMLParser
from typing import List, Optional, Dict


class Node:
    def __init__(self, tag: str, attrs: Optional[Dict[str, str]] = None, parent: 'Node' = None):
        self.tag: str = tag
        self.attrs: Dict[str, str] = attrs if attrs else {}
        self.text: str = ""          # immediate text inside this tag (not aggregated from children)
        self.children: List['Node'] = []
        self.parent: Optional['Node'] = parent

    def add_child(self, node: 'Node'):
        self.children.append(node)
        node.parent = self

    def __repr__(self):
        return f"Node(tag='{self.tag}', text='{self.text.strip()}', children={len(self.children)})"


class SimpleHTMLDOMParser(HTMLParser):

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node('document')
        self.stack: List[Node] = [self.root]
        # treat void elements (self-closing in HTML) that should not expect an endtag
        self.void_elements = {
            "area", "base", "br", "col", "embed", "hr", "img",
            "input", "link", "meta", "param", "source", "track", "wbr"
        }

    def handle_starttag(self, tag, attrs):
        # convert attrs list to dict
        attrs_dict = {k: v for (k, v) in attrs}
        node = Node(tag, attrs=attrs_dict)
        # add to current top of stack
        self.stack[-1].add_child(node)
        # push to stack except for void elements
        if tag.lower() not in self.void_elements:
            self.stack.append(node)
        # for void elements we don't push, they are leafs

    def handle_endtag(self, tag):
        # pop stack until matching tag found (to be tolerant to malformed HTML)
        tag = tag.lower()
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i].tag and self.stack[i].tag.lower() == tag:
                # pop everything above and including this index
                while len(self.stack) - 1 >= i:
                    self.stack.pop()
                return
        # if not found, ignore

    def handle_startendtag(self, tag, attrs):
        # self-closing tag like <br/>
        attrs_dict = {k: v for (k, v) in attrs}
        node = Node(tag, attrs=attrs_dict)
        self.stack[-1].add_child(node)
        # do not push

    def handle_data(self, data):
        if not data:
            return
        # attach data to current top node as immediate text
        current = self.stack[-1]
        # append, but normalize whitespace: collapse multiple whitespace into single space
        text = data.replace('\r', ' ').replace('\n', ' ')
        # strip leading/trailing but preserve one space separation when concatenating
        if text.strip():
            if current.text and not current.text.endswith(' '):
                current.text += ' '
            current.text += ' '.join(text.split())

    def handle_comment(self, data):
        # ignore comments, or optionally store as node:
        # comment_node = Node('!comment', {})
        # comment_node.text = data.strip()
        # self.stack[-1].add_child(comment_node)
        pass

    def handle_decl(self, decl):
        # handle <!DOCTYPE ...>
        doctype_node = Node('!doctype')
        doctype_node.text = decl.strip()
        self.stack[-1].add_child(doctype_node)

    def parse(self, html: str):
        # reset
        self.root = Node('document')
        self.stack = [self.root]
        self.feed(html)
        self.close()
        return self.root

def find_text_by_tag(root: Node, target_tag: str) -> List[str]:

    if not root:
        return []
    target = target_tag.lower()
    results: List[str] = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node.tag.lower() == target:
            if node.text.strip():
                results.append(node.text.strip())
        # extend with children
        for child in reversed(node.children):  # reversed to keep document order if using stack
            stack.append(child)
    return results

def print_dom_tree(node: Node, level: int = 0):

    if node is None:
        return
    indent = "  " * level
    attrs = ""
    if node.attrs:
        pairs = [f'{k}="{v}"' for k, v in node.attrs.items()]
        attrs = " " + " ".join(pairs)
    text = f" text='{node.text.strip()}'" if node.text.strip() else ""
    print(f"{indent}<{node.tag}{attrs}>{text}")
    for child in node.children:
        print_dom_tree(child, level + 1)
    # print closing tag marker for clarity except for document and void elements
    if node.tag not in ('document', '!doctype') and node.tag.lower() not in {'br', 'img', 'meta', 'link', '!comment'}:
        print(f"{indent}</{node.tag}>")

if __name__ == "__main__":
    html_document = r"""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
    <head>
        <meta http-equiv= "Content-Type" content= text/html; charset=windows-1251"> <title> Домашнє завдання. Парсинг DOM і сбереження в дереві.</title>
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
</html>
"""

    parser = SimpleHTMLDOMParser()
    root_node = parser.parse(html_document)

    print("\n--- DOM Tree ---")
    print_dom_tree(root_node)

    for tag in ('h2', 'title', 'p', 'meta'):
        print(f"\n--- Texts for tag '{tag}' ---")
        texts = find_text_by_tag(root_node, tag)
        if texts:
            for t in texts:
                print(f"Found: '{t}'")
        else:
            print("No text found for this tag.")