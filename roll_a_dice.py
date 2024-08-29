import random

print(random.randint(1,6))

while True:

    yn = input("do you want to go again?    ")

    if yn == "yes":
        print(random.randint(1,6))
    elif yn == "no":
        print("Ok, have a nice day!")
        break
    else:
        print('please say "yes" or "no"')