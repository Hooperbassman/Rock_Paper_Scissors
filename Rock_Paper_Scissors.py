print("Please enter rock, paper, or scissors ")
user_input = input().lower()
answer = user_input
import random
mylist = ["rock", "paper", "scissors"]
comp_answer = random.choice(mylist)

print ("You chose :", answer)
print("the computer chose :", comp_answer)

if answer == "rock" and comp_answer == "scissors":
    print("You win!")
elif answer == "rock" and comp_answer == "rock":
    print("Tie")
elif answer == "rock" and comp_answer == "paper":
    print("You lose!")
elif answer == "paper" and comp_answer == "rock":
    print("You win!")
elif answer == "paper" and comp_answer == "scissors":
    print("You lose!")
elif answer == "paper" and comp_answer == "paper":
    print("Tie")
elif answer == "scissors" and comp_answer == "paper":
    print("You win!")
elif answer == "scissors" and comp_answer == "rock":
    print("You lose!")
elif answer == "scissors" and comp_answer == "scissors":
    print("Tie")
else:
    print("Invalid input. Please enter rock, paper, or scissors.")




