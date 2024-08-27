import random


difficulty = input("Easy or Hard?"),strip().lower()
if difficulty == "easy":
    number = random.randint(1,100)
    x1 = input("I'm thinking of a number between 1 and 100, what do you think it is?").strip()
    
if x1<number:
    print("Too low!")
elif x1>number:
    print("Too high!")
    

    