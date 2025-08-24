def is_balanced(seq):
    stack = []
    openers = "([{"
    pairs = {')': '(', ']': '[', '}': '{'}

    for i, ch in enumerate(seq, 1):  # i — позиція (1..N), якщо захочеш для діагностики
        if ch in openers:
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack

def main():
    try:
        s = input("Введіть рядок: ")
    except EOFError:
        s = ""
    print("YES" if is_balanced(s) else "NO")

if __name__ == "__main__":
    main()