number = 5
user_input = input("Enter 'y' if you want to play': ").lower()

if user_input in ("y", "yes"):
    user_number = int(input("Enter your guess number: "))
    if user_number == 5:
        print("That's right!")
    elif user_number - number in (1, -1):
        print(f"Your choice is off by 1 ({user_number})")
    else:
        print("Your number is wrong")