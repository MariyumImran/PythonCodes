import numpy

num:int = 0
sum:int = 0
average:float = 0.0
times:int = int(input("How many numbers do you want to enter?   ").strip())

myNum:int

for i in range(times):
    num = int(input("Enter a number   ").strip())
    sum = num + sum

print("The sum of those numbers is:", sum)

average = (sum/times)
print("The Average is: ", average)