name = input("Enter your name: ")

age = input("Enter your age: ")
if age.isdigit():
    print(f"Hello, {name}, on your next birthday will be  {int(age) + 1} years.")
else: print("Ege must be digit")
