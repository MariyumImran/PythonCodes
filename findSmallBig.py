times:int
largest:int = 0
smallest:int

times = int(input("How many number do you want to enter?    "))
'''
fnum =  input("Enter a number    ")

if fnum == 0:
    for i in range(1,times):
        input("Enter a numbe    ").strip()
        print("0 is the smallest number")
else:
    smallest = int(fnum)

for i in range(1,times):
    num = int(input("Enter a number    ").strip())
    if num>largest:
        largest = num
        print (num)

print(int(num), "is the smallest number    ")

'''
#Babi's work
for i in range(times):
    fnum = int(input("Enter a number "))
    if i == 0:
        smallest = fnum
        largest = fnum
    else:
        if fnum < smallest:
            smallest = fnum
        if fnum > largest:
            largest = fnum

print(f"Smallest = {smallest} and largest = {largest}")
        












"""
    num = input ("Enter a number  ").strip()
    if int(num) > int(largest):
        largest = num
    
print(largest, "is the largest number")
"""