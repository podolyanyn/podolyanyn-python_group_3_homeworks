number=input("Enter phone number")
if len(number) !=10:
    print("Enter 10 digits")
else:
    if number.isdigit():
        print("number is right")
    else:
        print("number must be only with digits")
