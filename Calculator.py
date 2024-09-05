
print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice (1, 2, 3, 4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
     result = num1 + num2
elif choice == '2':
     result = num1 - num2
elif choice == '3':
    result = num1 * num2
elif choice == '4':
    result = num1 / num2
else:
    result = 'Error: say "1", "2", "3" or "4" '

print(result)