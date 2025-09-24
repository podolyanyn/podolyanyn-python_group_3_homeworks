class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, newdata):
        self.data = newdata

    def set_next(self, newnext):
        self.next = newnext


class UnsortedList:
    def __init__(self):
        self.head = None

    def __str__(self):

        items = []
        current = self.head
        while current is not None:
            items.append(str(current.get_data()))
            current = current.get_next()
        return "[" + ", ".join(items) + "]"

    def is_empty(self):
        return self.head is None

    def add(self, item):

        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):

        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):

        current = self.head
        while current is not None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def remove(self, item):

        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, item):

        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)

    def index(self, item):

        current = self.head
        pos = 0
        while current is not None:
            if current.get_data() == item:
                return pos
            current = current.get_next()
            pos += 1
        raise ValueError(f"{item} is not in list")

    def pop(self, pos=None):

        if self.is_empty():
            raise IndexError("pop from empty list")

        if pos is None:
            pos = self.size() - 1

        if pos < 0 or pos >= self.size():
            raise IndexError("list index out of range")

        current = self.head
        previous = None
        count = 0
        while count < pos:
            previous = current
            current = current.get_next()
            count += 1

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

        return current.get_data()

    def insert(self, pos, item):

        if pos < 0 or pos > self.size():
            raise IndexError("list index out of range")

        new_node = Node(item)
        if pos == 0:
            new_node.set_next(self.head)
            self.head = new_node
            return

        current = self.head
        previous = None
        count = 0
        while count < pos:
            previous = current
            current = current.get_next()
            count += 1

        new_node.set_next(current)
        previous.set_next(new_node)

    def slice(self, start, stop):

        if start < 0 or stop < 0 or start > self.size() or stop > self.size():
            raise IndexError("slice index out of range")

        new_list = UnsortedList()
        current = self.head
        pos = 0

        while current is not None and pos < start:
            current = current.get_next()
            pos += 1

        while current is not None and pos < stop:
            new_list.append(current.get_data())
            current = current.get_next()
            pos += 1

        return new_list

# --- Тестування ---
if __name__ == "__main__":
    my_list = UnsortedList()
    my_list.add(10)
    my_list.add(20)
    my_list.add(30)
    print("Initial list:", my_list)  # [30, 20, 10]

    # append
    my_list.append(5)
    print("After append(5):", my_list)  # [30, 20, 10, 5]

    # index
    print("Index of 20:", my_list.index(20))  # 1

    # insert
    my_list.insert(2, 25)
    print("After insert(2, 25):", my_list)  # [30, 20, 25, 10, 5]

    # pop last
    print("Pop last:", my_list.pop())  # 5
    print("After pop:", my_list)  # [30, 20, 25, 10]

    # pop at position
    print("Pop at position 1:", my_list.pop(1))  # 20
    print("After pop(1):", my_list)  # [30, 25, 10]

    # slice
    sliced = my_list.slice(1, 3)
    print("Slice (1, 3):", sliced)  # [25, 10]