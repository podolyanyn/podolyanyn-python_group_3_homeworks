import unittest

class CustomList:
    def __init__(self, items: list = None):
        self._items = list(items) if items is not None else []

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def append(self, item):
        self._items.append(item)


class TestCustomList(unittest.TestCase):
    def setUp(self):
        self.test_list = CustomList(['a', 'b', 'c'])

    def test_empty(self):
        empty_list = CustomList()
        self.assertEqual(len(empty_list), 0, "Empty list should have length 0")

    def test_init(self):
        self.assertEqual(len(self.test_list), 3, "Length should be 3")
        self.assertEqual(self.test_list[0], 'a', "First element 'a'")

    def test_iter(self):
        items = list(self.test_list)
        self.assertEqual(items, ['a', 'b', 'c'], "Iteration should give ['a', 'b', 'c']")

    def test_getitem(self):
        self.assertEqual(self.test_list[1], 'b', "Second element 'b'")
        self.assertEqual(self.test_list[-1], 'c', "Last element 'c'")

    def test_len(self):
        self.assertEqual(len(self.test_list), 3, "Length 3")

    def test_append(self):
        self.test_list.append('d')
        self.assertEqual(len(self.test_list), 4, "After append length 4")
        self.assertEqual(self.test_list[3], 'd', "New element 'd'")

if __name__ == "__main__":
    unittest.main(verbosity=2)