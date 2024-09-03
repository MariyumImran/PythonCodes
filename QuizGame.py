
score = 0

q1 = input ("What is the bigest planet?   ").strip()

if q1 == "Jupiter" or "jupiter":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

q2 = input ("What is the capital of Russia?   ").strip()

if q2 == "Moscow" or "moscow":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

q3 = input ("How much is a dozen?   ").strip()

if q3 == "12":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

print("Your score is...")
print(score, "/3")