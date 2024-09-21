import random

while True:
    user_choice = int(input("select the choice 0 for rock,1 for paper,2 for scissor"))
    computer_choice = random.randint(0, 2)
    print(f"computer choice{computer_choice}", computer_choice)
    if user_choice > 3 or user_choice < 0:
        print("take the value in the 0-2 range")
    else:
        if user_choice == computer_choice:
            print("draw")
        elif user_choice == 2 and computer_choice == 0:
            print("computer wins")
        elif user_choice == 0 and computer_choice == 2:
            print("user wins")
        elif user_choice > computer_choice:
            print("user wins")
        elif user_choice < computer_choice:
            print("computer wins")
    i=input("enter the letter to continue the game y/n")
    if i!="y" or i.lower()!="y":
        break





