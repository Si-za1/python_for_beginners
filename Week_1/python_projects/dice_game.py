#imports
import random

#Dice game via a player's input
user_choice = input("Do you want to play the rolling dice game? (y/n)").lower()

while True:

#when y game  starts 
    if user_choice == 'y':
        die_1 = random.randint(1,6)
        die_2 = random.randint(1,6)
        print(f"Your dices rolls as ({die_1}, {die_2})")
    #here the randint does include from 1 to 6

#when n game ends 
    elif user_choice == 'n':
        print("Thank you for your decision.")
        break
    
#when something else is given expect y or n invalid message 
    else:
        print("Please give your input with either y or n ")



