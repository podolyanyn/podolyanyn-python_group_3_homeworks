import random
#  random number  1 to  10
computer_number = random.randint(1, 10)
# ask the user to enter a number
user_number = int(input("guess the number 1 to 10: "))
if user_number > 10 or user_number < 1:
    print("The number must be > 0 and <=10")
else:
    if user_number == computer_number:
        print("Congratulation you guessed number")
    else:
        print(f"Sorry, you didn't guess, computer number:  {computer_number}.")