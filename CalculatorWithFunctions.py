def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b
    
def main():
    while True:
        
        res = 0
        print("Do you want to add, substract, multiply or divide?")
        op = int(input("Type 1 for addision, 2 for substraction, 3 for multiplication, 4 for division and 0 to quit    "))
        if op == 1:
            a = int(input("what is the first number you want to add?    "))
            b = int(input("what is the second number you want to add?    "))
            res = add(a,b)
            print(res)
            
        elif op == 2:
            a = int(input("what is the first number you want to substract?    "))
            b = int(input("what is the second number you want to substract?    "))
            res = sub(a,b)
            print(res)
            
        elif op == 3:
            a = int(input("what is the first number you want to multiply?    "))
            b = int(input("what is the second number you want to multiply?    "))
            res = mul(a,b)
            print(res)
            
        elif op == 4:
            a = int(input("what is the first number you want to divide?    "))
            b = int(input("what is the second number you want to divide?    "))
            res = div(a,b)
            print(res)

        elif op == 0:
            break

        else:
            print("Invalid, please try again")
            

if __name__ == '__main__':
    main()


#started at 11:00, ended at 01:30