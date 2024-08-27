import random

min:int = 1
max:int = 100
num:int = 0
num = random.randint(min, max)



while True:
    guess = int(input("Guess a number between 1 to 100 (or press cntr + c to e "))
    #guess2 = "int(input("Guess a number between 1 to 100:    "))"

    if guess == num:
            print("Congratulations! You guessed the correct number.")
    elif guess < num:
            print ("Too low. Try again.")
            #print("Guess a number between 1 to 100:    ")
    else:
            print ("Too high. Try again.")
            #printinput("Guess a number between 1 to 100:    ")