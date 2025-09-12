class Stack:

    def __init__(self):
        self._items = []

    def is_empty(self) -> bool:
        return not self._items

    def push(self, item) -> None:
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self._items.pop()


def are_brackets_balanced(sequence: str) -> bool:

    stack = Stack()

    bracket_map = {")": "(", "}": "{", "]": "["}
    opening_brackets = set(bracket_map.values())

    for char in sequence:
        if char in opening_brackets:
            stack.push(char)
        elif char in bracket_map:
            if stack.is_empty():
                return False
            if stack.pop() != bracket_map[char]:
                return False

    return stack.is_empty()


# --- Main program logic ---
if __name__ == "__main__":
    print("Enter a sequence of characters to check for balanced brackets (e.g., '{[()]}'):")
    user_input = input()

    if are_brackets_balanced(user_input):
        print(f"The sequence '{user_input}' has balanced brackets.")
    else:
        print(f"The sequence '{user_input}' does NOT have balanced brackets.")

    # --- Quick tests ---
    print("\nRunning quick tests...")
    assert are_brackets_balanced("{[()]}") == True
    assert are_brackets_balanced("{[(])}") == False
    assert are_brackets_balanced("((()))") == True
    assert are_brackets_balanced("(()") == False
    assert are_brackets_balanced("") == True
    print("All tests passed!")
