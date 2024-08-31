import random

choices = ["rock", "scissors", "paper"]
user = input("Enter rock, paper or scissors ").lower()
comp = random.choice(choices)

print("you chose",(user))
print("I chose", (comp))

if user == comp:
    print("It's a tie!")
elif user == "rock" and comp == "paper" or \
     user == "paper" and comp == "scissors" or \
     user == "scissors" and comp == "rock":
    print("You win!")
else:
    print("You Lost!")