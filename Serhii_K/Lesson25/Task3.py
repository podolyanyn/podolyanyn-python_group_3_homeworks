# Task 3:
# Реалізувати чергу з використанням однозв'язного списку.

from Task1 import Node, linkedlist

class MyQueue:
    def __init__(self):
        self.my_queue = linkedlist()

    def unqueue(self, data):
        self.my_queue.insert(0,data)

    def dequeue(self):
        return self.my_queue.pop()

    def is_empty(self):
        return self.my_queue.size() == 0

    def size(self):
        return self.my_queue.size()

    def __str__(self):
        return self.my_queue.__str__()

# Використання:
if __name__ == '__main__':
    q = MyQueue()
    q.unqueue(1)
    q.unqueue(2)
    q.unqueue(3)
    q.unqueue(4)
    q.unqueue(5)
    print(q.__str__())

    print(f"Size queue: {q.size()}")    # 5

    print(f"queue.dequeue: {q.dequeue()}")
    print(f"queue.dequeue: {q.dequeue()}")
    print(q.__str__())
    print(f"queue.empty: {q.is_empty()}")


