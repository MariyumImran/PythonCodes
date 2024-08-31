print ("Hello, to login, please enter the password")
password = input("pasword?    ")

if len (password) < 8:
    print("wrong, please try again")
else:
    print("Correct password, you may login now")