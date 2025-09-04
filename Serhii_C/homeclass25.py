# Завдання 1
#
# Розширення несортованого списку
#
# Реалізуйте методи додавання, індексування, вилучення та вставки для несортованого списку.
# Також реалізуйте метод зрізу, який прийматиме два параметри «старт» та «стоп» і повертатиме копію списку,
# починаючи з позиції та до позиції зупинки, але не включаючи її.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def __str__(self):
        result = ''
        current = self.head
        while current:
            result += str(current.data) + ' | '
            current = current.next
        return result

    def search(self,data):
        current = self.head
        while current:
            if data == current.data:
                return True
            else:
                current = current.next
        return False

    def remove(self,data):
        previous = None
        current = self.head
        if data == self.head.data:
            self.head = self.head.next

        else:

            while current:

                if current.data == data:
                    previous.next = current.next
                    return

                else:
                    previous = current
                    current = current.next

    def add_tail(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def insert(self, data,place):
        new_node = Node(data)
        current = self.head
        previous = None
        if self.head.data == place:
            current= self.head.next
            self.head = new_node
            new_node.next = current
            return




        else:
            current = self.head
            previous = None
            while current.next:
                previous = current
                current = current.next
                if current.data == place:
                    previous.next = new_node
                    new_node.next = current
                    return

    def remove_front(self):
        self.head = self.head.next

    def remove_tail(self):
        result = self.head
        previous = None
        while result.next:
            previous = result
            result = result.next


        previous.next = None

    def index_list(self):
        current = self.head
        current_index = 0
        index_list = []
        while current:
            index_list.append(current.data)
            current = current.next
        for i in enumerate(index_list):
            print(i)

    def search_index(self, data):
        current = self.head
        current_index = 0
        index_list = []
        while current:
            index_list.append(current.data)
            current = current.next
        b = False
        for i in index_list:

            if i == data:
                print(f'Element {i} has index {current_index}')
                b = True

            current_index += 1
        if b == False:
            print(f'Element {data} has not been found')

    def slice(self, start, end):
        current = self.head
        index_list = []
        while current:
            index_list.append(current.data)
            current = current.next

        sliced_list = index_list[start-1:end]
        return sliced_list


linked_list = LinkedList()
linked_list.add(1)
linked_list.add(2)
linked_list.add(10)
print(linked_list)
print(linked_list.search(2))
# linked_list.remove(2)
# linked_list.remove(10)
linked_list.add_tail(8)
print(linked_list)
# linked_list.remove(8)
print(linked_list)
linked_list.insert(5,2)
linked_list.insert(4,1)
linked_list.insert(3,10)
linked_list.insert(11,8)
linked_list.insert(12,3)
print(linked_list)
linked_list.remove_front()
linked_list.remove_tail()
print(linked_list)
print(linked_list.index_list())
linked_list.search_index(1)
linked_list.search_index(1122)
print(linked_list.slice(2,8))
linked_list.insert(9,11)
print(linked_list)

# Task 2
#
# Implement a stack using a singly linked list.

# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList(object):
#     def __init__(self):
#         self.head = None
#
#     def add(self, data):
#         if self.head is None:
#             self.head = Node(data)
#         else:
#             new_node = Node(data)
#             new_node.next = self.head
#             self.head = new_node
#
#     def __str__(self):
#         result = ''
#         current = self.head
#         while current:
#             result += str(current.data) + ' | '
#             current = current.next
#         return result
#
#     def remove_front(self):
#         self.head = self.head.next
#
# linked_list = LinkedList()
# linked_list.add(1)
# linked_list.add(2)
# linked_list.add(10)
# print(linked_list)
# linked_list.remove_front()
# print(linked_list)

# Task 3
#
# Implement a queue using a singly linked list.


# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList(object):
#     def __init__(self):
#         self.head = None
#
#     def add(self, data):
#         if self.head is None:
#             self.head = Node(data)
#         else:
#             new_node = Node(data)
#             new_node.next = self.head
#             self.head = new_node
#
#     def __str__(self):
#         result = ''
#         current = self.head
#         while current:
#             result += str(current.data) + ' | '
#             current = current.next
#         return result
#
#     def remove_tail(self):
#         result = self.head
#         previous = None
#         while result.next:
#             previous = result
#             result = result.next
#
#             print(result.data)
#         previous.next = None
#
#
# linked_list = LinkedList()
# linked_list.add(1)
# linked_list.add(2)
# linked_list.add(10)
# print(linked_list)
# linked_list.remove_tail()
# linked_list.remove_tail()
# print(linked_list)


