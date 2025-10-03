import random
String = input("Enter String: ")
if len(String)==0 or not String.isalpha():
    print("Enter word again")
else:

    print("Random combinations:")
    for i in range(len(String)):
        mixed_word = "".join(random.sample(String, len(String)))
        print(mixed_word)
