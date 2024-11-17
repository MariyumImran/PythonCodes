#   This project converts binary code to decimals
#   Mariyum Imran
#   16th of November 2024(saturday)

while True:
    #input number
    number = str(input("Enter a Binary number:    "))
    #check if binary
    print(number)
    cntr = 0
    for i in number:
        i = int(i)
        if i == 1 or i == 0:
            cntr +=1
        else:
            print("That is not a binary number. A binary number is a number that only has ones and zeros. Please try again.")
            break
    if cntr == len(number):
        break
   
#convert to deci

len = len(number)
dec = 0

for counter, i in enumerate(number):
    i = int(i)
    ad = pow(2,len - counter - 1)
    hi = ad * i
    dec += hi

#print number

print("The decimal number for ", number, "is:    ",dec)

#started at 1:30,  ended  at 01:10, total 1 1hr 40mins
#started at 02:00, paused at 03:10, total 2 1hr 10mins 
#resumed at 05:40, ended  at 06:20, total 2 0hr 40mins