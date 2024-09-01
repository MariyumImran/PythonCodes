
text = input("Enter some text:  ")
numOfVowels = 0
vowels = "aeiouAeiou"

for i in text:
    if i in vowels:
        numOfVowels = numOfVowels + 1

print ("There are", numOfVowels, "vowels")