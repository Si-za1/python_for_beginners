# imports
import random

# asks user to input the choice to play y or n
user_game_choice = input("Do you want to play or not (y/n): ").lower()

while True:
    # if choice  is  y and 1 then
    if user_game_choice == 'n':
        print("Thank you for your decision")
        break

    elif user_game_choice == 'y':
        # ask user to how many dice to roll 1 or 2
        user_dice_choice = int(input("How many dices do you want to play with? 1 or 2: "))

        if user_dice_choice == 1:
            dice_1 = random.randint(1, 6)
            print(f" Your dice results in {dice_1}")
            break

        # if choice is y and 2 then
        elif user_dice_choice == 2:
            dice_1 = random.randint(1, 6)
            dice_2 = random.randint(1, 6)
            print(f"Your dice results as ({(dice_1, dice_2)})")
            break

    else:
        print("Please input something valid to start the game")
