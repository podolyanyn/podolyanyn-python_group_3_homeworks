def revers():
    text = input("Введіть послідовність символів: ")

    stack = []

    for ch in text:
        stack.append(ch)

    reversed_text = ""
    while stack:
        reversed_text += stack.pop()  #

    print("Рядок у зворотному порядку:", reversed_text)
revers()

