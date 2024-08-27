
num = int(input("Enter a number  ").strip())

R = num % 2

#print("The remainder is", R)

if R == 0:
    print("The number is even")
else: 
    print("The number is odd")

IsPrime = True

for i in range(2, num):
    if (num % i) == 0:
        IsPrime = False
        
if IsPrime == True:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number"
          