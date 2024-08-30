#Change Return Program - The user enters a cost and then the amount of money given. The program will figure out the change and the
#  number of toonies, loonies, quarters, dimes, nickels, pennies needed for the change.

cost = float(input("How much does it cost?    "))
moneyGiven = float(input("How much money was given?    "))
change = moneyGiven - cost

#change*100 makes dollars into cents: 3.75 dollars = 375 cents, and "round" rounds it up: 375.8 = 376
changeCents = round(change*100)

#print(changeCents)

#how many $100 notes needed for change
hundred = changeCents // 10000

if hundred > 0:
    print("You need",int(hundred), "$100 notes")

#gets rid of everything other than the remainder
changeCents %= 10000

#how many $50 notes needed for change
fifty = changeCents // 5000

if fifty > 0:
    print("You need",int(fifty), "$50 notes")
changeCents %= 5000

#how many $10 notes needed for change
ten = changeCents // 1000

if ten > 0:
    print("You need",int(ten), "$10 notes")
changeCents %= 1000

#how many $5 notes needed for change
five = changeCents // 500

if five > 0:
    print("You need",int(five), "$5 notes")
changeCents %= 500

#how many toonies($2) notes needed for change
toonies = changeCents // 200

if toonies > 0:
    print("You need",int(toonies), "toonies($2)")
changeCents %= 200

#how many loonies notes needed for change
loonies = changeCents // 100

if loonies > 0:
    print("You need",int(loonies), "loonies($1)")
changeCents %= 100

#how many quaters notes needed for change
quaters = changeCents // 25

if quaters > 0:
    print("You need",int(quaters), "quaters(25 cents)")
changeCents %= 25

#how many dimes notes needed for change
dimes = changeCents // 10

if dimes > 0:
    print("You need",int(dimes), "dimes(10 cents)")
changeCents %= 10

#how many nickels notes needed for change
nickels = changeCents // 5

if nickels > 0:
    print("You need",int(nickels), "nickels(5 cents)")
changeCents %= 5

#how many pennies notes needed for change
pennies = changeCents // 1

if pennies > 0:
    print("You need",int(pennies), "pennies(1 cents)")
changeCents %= 1
