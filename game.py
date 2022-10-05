#1 Start
#2 display rock paper scizzers
#3 Ask user what he wanna choose
#4 Let the computer to make choice using random numbers
#5 Display Result
#6 Stop
import random
import os
from time import sleep

def user_move(str):
    if str=="Rock":
        return 1
    elif str=="Paper":
        return 2
    else :
        return 3



print("********* Welcome to Rock Paper Scissors Game *********")
print()
sleep(1)
print("Rock")
sleep(1)
print("Paper")
sleep(1)
print("Scissors")
sleep(1)
user=input("What you choose: ")
computer=random.randrange(1,3)
print()

if user_move(user)==1  and computer==2 :
    print("Your move - Rock" )
    sleep(1)
    print("Computer's move - Paper")
    sleep(1)
    print("Whoops! Computer win")
elif user_move(user)==2 and computer==3:
    print("Your move - Paper")
    sleep(1)
    print("Computer's move - Scissors")
    sleep(1)
    print("Whoops! Computer win")
elif user_move(user)==3 and computer==1:
    print("Your move - Scissors")
    sleep(1)
    print("Computer's move - Rock ")
    sleep(1)
    print("Whoops! Computer win")
elif computer==1  and user_move(user)==2:
    print("Your move - Paper")
    sleep(1)
    print("Computer's move - Rock ")
    sleep(1)
    print("******* You Won! ********")
elif computer==2  and user_move(user)==3:
    print("Your move - Scissors")
    sleep(1)
    print("Computer's move - Paper ")
    sleep(1)
    print("******* You Won! ********")
elif computer==3 and user_move(user)==1:
    print("Your move - Rock")
    sleep(1)
    print("Computer's move - Scissors ")
    sleep(1)
    print("******* You Won! ********")
    print()
elif computer == 3 and user_move(user) == 3:
    print("Your move - Scissors")
    sleep(1)
    print("Computer's move - Scissors ")
    sleep(1)
    print("----- Tie ------")
elif computer == 2 and user_move(user) == 2:
    print("Your move - Paper")
    sleep(1)
    print("Computer's move - Paper ")
    sleep(1)
    print("----- Tie ------")
elif computer == 1 and user_move(user) == 1:
    print("Your move - Rock")
    sleep(1)
    print("Computer's move - Rock")
    sleep(1)
    print("----- Tie ------")