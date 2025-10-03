x = 11
y = 10
right_answer = x + y
print(f"how much will it be: {x} + {y}?")
answer= input("Your answer: ")
if answer.isdigit():
    if int(answer) == right_answer:
        print("ok")
    else:
        print(f"Not right: {right_answer}")
else:
    print("Enter digit")