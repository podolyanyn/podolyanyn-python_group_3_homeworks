from typing import List


# A simple implementation of a Stack
class Stack:

    def __init__(self):
        self._items: List[str] = []

    def is_empty(self) -> bool:
        return not self._items

    def push(self, item: str) -> None:
        self._items.append(item)

    def pop(self) -> str:

        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def clear(self) -> None:
        self._items.clear()


def reverse_string(s: str) -> str:
    char_stack = Stack()

    for char in s:
        char_stack.push(char)

    reversed_chars = []
    while not char_stack.is_empty():
        reversed_chars.append(char_stack.pop())

    return "".join(reversed_chars)


if __name__ == "__main__":
    print("Enter a sequence of characters to be reversed (press Enter when done):")

    input_string = input()
    reversed_string = reverse_string(input_string)

    print("\nOriginal sequence:")
    print(input_string)

    print("\nReversed sequence:")
    print(reversed_string)