# Task 1:
# Розширити структуру, яку побудували на уроці,
# можливістю вставки дерева в наявне дерево та видалення піддерева з дерева, що існує.

# Я переробив дерево так, щоб кожний вузел вставлявся в відсортованому порядку

class Node:
    def __init__(self, data):
        self.data = data
        # В якості ключа використовуємо хеш (це дозволяє отримувати ключі не тільки від чисел.
        # І також дозволяє порівнювати ключи і сортувати по значенню ключа.
        # Але звісно порівнювати значення різних типів неможливо)
        self.key = hash(data)
        self.left = None
        self.right = None
        self.level = None

class Tree:
    def __init__(self, data=None):
        self.root = None
        if data is not None:
            self.insert(Node(data), None)

    def show(self, node, level = 0):
        """Метод, що преобразовує дерево в візуальний рядок для подальшого принта
         (рекурсивно обходить вузли і повертає їх значеня)"""
        res = ''
        shift = ''
        if node:
            # Розрахунок відступ тексту залежно від рівня вузла (чим глибше в дереві вузел - тим більше відступ)
            if level == 0:
                shift_root = ''         # відступ перед корнем
                shift_l_r = '       '   # відступ перед лівим та правим нащадками
            else:
                shift_root = '       ' * level
                shift_l_r = '       ' * (level + 1)
            # Підготовка рядків з значенням вузла, а також лівого та правого нащадків:
            root = str(node.data)
            left = self.show(node.left, level + 1)
            right = self.show(node.right, level + 1)
            # Формування підсумкового рядка
            res = f"[Root:{root}\n{shift_l_r}l:{left}\n{shift_l_r}r:{right}\n{shift_root}  ]"
        else:
            res = 'None'
        return res

    def __str__(self):
        return self.show(self.root)

    def insert(self, new_node, node=None):
        """Метод, що кріпить новий вузел до наявного узла в дереві в залежності від значення їх ключа, тобто одразу сортує дерево"""
        # Якщо батьківський вузел не передано, то приймаємо що це корінь дерева
        if node is None:
            node = self.root
        # Якщо вставляється не вузол, а якісь дані,
        # то потрібно створити новий екземпляр вузла
        if not isinstance(new_node, Node):
            new_node = Node(new_node)

        # Якщо дерево ще пусте - то робимо цей перший вузол як корінь дерева:
        if self.root is None:
            self.root = new_node
            self.root.level = 0
        else:
            # Якщо значення ключа нового вузла дорівнює значенню ключа поточного вузла,
            # то вставка не потрібна, щоб не створювати дублікати
            # (викликаємо помилку, бо не ясно чи потрібно замінювати дані по даному ключу, чи ні....
            # Хоча якщо працюємо сугубо з числами, то можна було б просто нічого не робити...)
            if new_node.key == node.key:
                raise ValueError('Вузол з таким значенням вже є в дереві!')

            # Далі потрібно вирішити куди вставляти новий вузел:
            # Якщо значення ключа меньше за значення ключа поточного вузла - вставляти будемо в ліву гілку
            elif new_node.key < node.key:
                # Якщо в лівій гілці ще немає вузла - кріпимо новий вузол до лівої гілки
                if node.left is None:
                    node.left = new_node
                # Інакше - рекурсивно спускаємось по лівій гілці і кріпимо новий вузел десь там..:
                else:
                    self.insert(new_node, node.left)

            # Якщо значення ключа більш за значення ключа поточного вузла - вставляти будемо в праву гілку
            elif new_node.key > node.key:
                # Якщо в правій гілці ще немає вузла - кріпимо новий вузол до правої гілки
                if node.right is None:
                    node.right = new_node
                # Інакше - рекурсивно спускаємось по лівій гілці і кріпимо новий вузел десь там..:
                else:
                    self.insert(new_node, node.right)

    def search(self, value, node=None, parent_node=None ):
        """Метод пошуку вузла з заданим значенням.
        Рекурсивно проходить по дереву, порівнюючи значення кожного вузла,
        і якщо шукане значення менше поточного - спускаємось лівою гілкою,
        і навпаки якщо шукане значення більше поточного - ідемо правою гілкою.
        Також цей метод використовується при видалені вузлів"""

        # Перевірка чи вузел node одразу має значення None
        if node is None:
            return False, None, parent_node
        # Якщо шукане значення знаходиться в поточному вузлі,
        # то повертаємо посилання на вузел, посилання на батьківський вузел,
        # а також булевий флаг того, що вузел знайдено)
        if value == node.key:
            # Повертаємо вузол, батьківський вузол
            # і True (флаг того, що шукане значення знайдене в цій віршині (вузлі))
            return True, node, parent_node
        # Якщо шукане значення меньше того, що знаходиться в поточному вузлі -
        # потрібно рекурсивно йти лівою стороною (якщо існує лівий потомок)
        if value < node.key:
            if node.left:
                return self.search(value, node.left, node)
        # Якщо шукане значення більшо того, що знаходиться в поточному вузлі -
        # потрібно рекурсивно йти правою стороною (якщо існує правий потомок)
        if value > node.key:
            if node.right:
                return self.search(value, node.right, node)
        # Повертаємо False (флаг того, що вузла з шуканим значенням не знайдено),
        # а також вузол (до якого будемо добавляти новий вузол), батьківський вузол
        return False, node, parent_node

    def find(self, value):
        """Метод, що повертає булеве значення чи є шукане значення в дереві, чи ні"""
        # # Спочатку потрібно отримати ключ для пошуку (хеш шуканого значення)
        # text = str(value)  # будь-що переводимо у рядок
        # key = hashlib.sha256(text.encode()).hexdigest()
        key = hash(value)

        flag, node, parent_node = self.search(key, self.root, None )
        return flag

    def find_min(self, node, parent_node):
        """Метод, що рекурсивно проходить по правій гілці, і шукає крайній лівий вузел (вузел з мінімальним значенням)"""
        if node.left:
            return self.find_min(node.left, node)
        return node, parent_node

    def del_node(self, value):
        # # Спочатку потрібно отримати ключ для пошуку (хеш шуканого значення)
        # text = str(value)  # будь-що переводимо у рядок
        # key = hashlib.sha256(text.encode()).hexdigest()
        key = hash(value)

        flag, node, parent_node = self.search(key, self.root, None )

        # Якщо flag_find == False, то вершина (вузол) з шуканим значенням не була знайдена
        if not flag:
            return None

        # 1 ситуація - вершина s листова (тобто у видаляємого вузла немає обох нащадків):
        if node.left is None and node.right is None:
            # parent - батьківська вершина для видаляємої вершини node
            if parent_node is None:  # Якщо в корні тільки один вузел
                self.root = None
            elif parent_node.left == node:
                parent_node.left = None
            elif parent_node.right == node:
                parent_node.right = None

        # 2 ситуація - видалення вершини з існуючим правим або лівим нащадком (тільки з одним нащадком):
        elif node.left is None or node.right is None:
            # Якщо видаляємо корінь
            if parent_node is None:
                if node.left:
                    self.root = node.left
                elif node.right:
                    self.root = node.right
            else:
                # Інакше, якщо видаляємо не корінь
                # Перевіряємо з якої сторони батьківського вузла знаходиться видаляємий вузел
                # і з якої сторони у нього прикріплен наступний вузол,
                # і перепризначаємо посилання від батьківського вузла одразу до вузла-нащадка
                if parent_node.left == node:
                    if node.left is None:
                        parent_node.left = node.right
                    elif node.right is None:
                        parent_node.right = node.left
                elif parent_node.right == node:
                    if node.right is None:
                        parent_node.right = node.left
                    elif node.left is None:
                        parent_node.right = node.right


        # 3 ситуація - видалення вершини з обома нащадками.
        # При цьому замість видаляємого вузла має бути вставлений вузул з тих,
        # що мають БІЛЬШЕ значення, ніж у видаляємого вузла (тобто з правої гілки),
        # але з НАІМЕНЬШИМ значенням (тобто наіменьший вузел з правої гілки):
        else:
            # Шукаємо мінімальний вузол у правому піддереві від видаляємого вузла
            node1, parent_node1 = self.find_min(node.right, node)
            # Копіюєм дані цього вузла в видаляємий вузел
            # (по суті ми видаляти не будемо, а тільки замінимо дані вузла)
            node.key = node1.key
            node.data = node1.data
            # Видаляємо вузел (мінімум)
            if parent_node1.left == node1:
                parent_node1.left = node1.right
            else:
                parent_node1.right = node1.right


# Використання:
if __name__ == '__main__':
    # Створення дерева
    t = Tree()
    t.insert(100)
    t.insert(50)
    t.insert(150)
    t.insert(75)
    t.insert(175)
    t.insert(25)
    t.insert(125)
    print(t)

    # Видалення вузла:
    t.del_node(175)     # Видалення листового вузла
    t.del_node(50)      # Видалення вузла з одним нащадком
    t.del_node(100)     # Видалення коріня / вузла з двома нащадками
    print(t)